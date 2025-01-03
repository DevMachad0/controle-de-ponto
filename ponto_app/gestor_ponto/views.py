from django.shortcuts import render, redirect, get_object_or_404
from .models import Empresa, Ponto, Funcionario
from .forms import FuncionarioForm
from django.utils.timezone import now
from datetime import datetime
from django.db.models import Q

def index(request): # Exibe a lista de empresas na página inicial
    empresas = Empresa.objects.all()
    return render(request, '../templates/index.html', {'empresas': empresas})

def cadastrar_empresa(request): # Cadastra uma nova empresa no sistema
    if request.method == 'POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')

        if not Empresa.objects.filter(nome=nome).exists():
            Empresa.objects.create(nome=nome, endereco=endereco)
            return redirect('index')

    return render(request, 'cadastrar_empresa.html')

def selecionar_empresa(request): # Processa a seleção de uma empresa para ser visualizada
    if request.method == 'POST':
        empresa_id = request.POST.get('empresa')
        return redirect('pagina_empresa', empresa_id=empresa_id)

def pagina_empresa(request, empresa_id): # Exibe os detalhes de uma empresa específica
    empresa = get_object_or_404(Empresa, id=empresa_id)
    return render(request, 'empresa.html', {'empresa': empresa})

def registrar_ponto(request, empresa_id): # Registra o ponto de entrada ou saída de um funcionário para uma empresa
    empresa = get_object_or_404(Empresa, id=empresa_id)
    erro = None

    if request.method == 'POST':
        funcionario_input = request.POST.get('funcionario')
        tipo = request.POST.get('tipo')
        
        try:
            funcionario = Funcionario.objects.get(email=funcionario_input, empresa=empresa)
            horario_atual = datetime.now()
            data_atual = horario_atual.date()

            if tipo == 'entrada':
                entrada_existente = Ponto.objects.filter(funcionario=funcionario, data=data_atual, entrada__isnull=False).exists()
                if entrada_existente:
                    erro = 'Já existe uma batida de entrada para este funcionário hoje.'
                else:
                    Ponto.objects.create(funcionario=funcionario, data=data_atual, entrada=horario_atual)
                    return redirect('pagina_empresa', empresa_id=empresa.id)
            
            elif tipo == 'saida':
                ponto = Ponto.objects.filter(funcionario=funcionario, data=data_atual).last()
                if not ponto or not ponto.entrada:
                    erro = 'Não é possível registrar a saída sem uma entrada previamente registrada.'
                elif ponto.saida:
                    erro = 'A saída já foi registrada para este funcionário hoje.'
                else:
                    ponto.saida = horario_atual
                    ponto.save()
                    return redirect('pagina_empresa', empresa_id=empresa.id)
        except Funcionario.DoesNotExist:
            erro = 'Funcionário não encontrado para esta empresa.'

    return render(request, 'registrar_ponto.html', {'empresa': empresa, 'erro': erro})

def registro_batidas(request, empresa_id): # Exibe e filtra os registros de ponto dos funcionários de uma empresa
    empresa = get_object_or_404(Empresa, id=empresa_id)
    registros = Ponto.objects.filter(funcionario__empresa=empresa).order_by('-data', '-entrada')
    query_nome = request.GET.get('nome')
    query_data = request.GET.get('data')
    
    if query_nome:
        registros = registros.filter(funcionario__nome__icontains=query_nome)
    if query_data:
        try:
            data_filtro = datetime.strptime(query_data, "%Y-%m-%d").date()
            registros = registros.filter(data=data_filtro)
        except ValueError:
            pass

    return render(request, 'registro_batidas.html', {
        'empresa': empresa,
        'registros': registros,
        'query_nome': query_nome,
        'query_data': query_data
    })

def funcionarios(request, empresa_id): # Exibe e permite o cadastro de funcionários para uma empresa
    empresa = Empresa.objects.get(pk=empresa_id)
    funcionarios = Funcionario.objects.filter(empresa=empresa)

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.empresa = empresa
            funcionario.save()
            return redirect('funcionarios', empresa_id=empresa_id)
    else:
        form = FuncionarioForm()

    return render(request, 'funcionarios.html', {
        'empresa': empresa,
        'form': form,
        'funcionarios': funcionarios,
    })
