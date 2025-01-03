import sqlite3
from datetime import datetime, timedelta

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Apagar os dados existentes
cursor.execute("DELETE FROM gestor_ponto_ponto")
cursor.execute("DELETE FROM gestor_ponto_funcionario")
cursor.execute("DELETE FROM gestor_ponto_empresa")
conn.commit()

# Função para popular o banco de dados
def popular_dados():
    # Criar empresas
    empresas = [
        ("Tech Solutions Ltda", "Rua das Flores, 123 - São Paulo, SP"),
        ("Alpha Construções", "Avenida Paulista, 456 - São Paulo, SP"),
        ("Beta Saúde", "Rua dos Médicos, 789 - Rio de Janeiro, RJ"),
    ]

    for nome, endereco in empresas:
        cursor.execute("INSERT INTO gestor_ponto_empresa (nome, endereco) VALUES (?, ?)", (nome, endereco))

    # Obter IDs das empresas
    cursor.execute("SELECT id FROM gestor_ponto_empresa")
    empresa_ids = [row[0] for row in cursor.fetchall()]

    # Criar funcionários
    funcionarios = [
        ("João Silva", "joao.silva@techsolutions.com", empresa_ids[0]),
        ("Maria Oliveira", "maria.oliveira@techsolutions.com", empresa_ids[0]),
        ("Carlos Pereira", "carlos.pereira@alphaconstrucoes.com", empresa_ids[1]),
        ("Ana Santos", "ana.santos@alphaconstrucoes.com", empresa_ids[1]),
        ("Fernanda Costa", "fernanda.costa@betasaude.com", empresa_ids[2]),
        ("Ricardo Almeida", "ricardo.almeida@betasaude.com", empresa_ids[2]),
    ]

    for nome, email, empresa_id in funcionarios:
        cursor.execute("INSERT INTO gestor_ponto_funcionario (nome, email, empresa_id) VALUES (?, ?, ?)", (nome, email, empresa_id))

    # Obter IDs dos funcionários
    cursor.execute("SELECT id FROM gestor_ponto_funcionario")
    funcionario_ids = [row[0] for row in cursor.fetchall()]

    # Criar batidas de ponto
    hoje = datetime.now()
    batidas = [
        (funcionario_ids[0], hoje.date(), hoje.replace(hour=9, minute=0, second=0).time(), hoje.replace(hour=18, minute=0, second=0).time()),
        (funcionario_ids[1], hoje.date(), hoje.replace(hour=8, minute=30, second=0).time(), hoje.replace(hour=17, minute=30, second=0).time()),
        (funcionario_ids[2], hoje.date(), hoje.replace(hour=9, minute=15, second=0).time(), None),  # Sem saída
        (funcionario_ids[3], hoje.date(), hoje.replace(hour=10, minute=0, second=0).time(), hoje.replace(hour=16, minute=0, second=0).time()),
        (funcionario_ids[4], hoje.date(), hoje.replace(hour=7, minute=45, second=0).time(), hoje.replace(hour=15, minute=30, second=0).time()),
        (funcionario_ids[5], hoje.date(), hoje.replace(hour=9, minute=0, second=0).time(), hoje.replace(hour=18, minute=0, second=0).time()),
    ]

    for funcionario_id, data, entrada, saida in batidas:
        cursor.execute(
            "INSERT INTO gestor_ponto_ponto (funcionario_id, data, entrada, saida) VALUES (?, ?, ?, ?)",
            (funcionario_id, data, entrada, saida),
        )

    conn.commit()
    print("Dados populados com sucesso!")

# Executar a função de popular dados
popular_dados()

# Fechar a conexão com o banco de dados
conn.close()
