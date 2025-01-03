# ponto_app/gestor_ponto/forms.py
from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'email']  # Não incluir 'empresa', pois é atribuído automaticamente na view
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do funcionário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o email do funcionário'}),
        }