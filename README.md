# Sistema de Controle de Ponto

Um sistema simples de controle de ponto para empresas, desenvolvido em Django. Permite o cadastro de empresas e funcionários, além do registro e consulta de batidas de ponto, com cálculo automático de horas trabalhadas.

---

## 📋 Funcionalidades

### 1. Gestão de Empresas
- Cadastro de empresas com campos como nome e endereço.
- Listagem e visualização das empresas cadastradas.

### 2. Gestão de Funcionários
- Associados às empresas.
- Campos como nome e e-mail.
- Cada funcionário pode registrar seus pontos de entrada e saída.

### 3. Registro de Ponto
- Registro de entrada e saída para funcionários.
- Cálculo automático de horas trabalhadas entre os horários registrados.

### 4. Consulta de Registros
- Filtragem por nome do funcionário.
- Filtragem por data.
- Exibição em uma tabela com as seguintes informações:
  - Funcionário
  - Data
  - Entrada
  - Saída
  - Horas Trabalhadas

---

🚀 Como Usar
Pré-requisitos Python 3.11 ou superior. Ambiente virtual configurado. Dependências instaladas.

Instalação
Clone este repositório:

git clone https://github.com/seu-usuario/controle-de-ponto.git
cd controle-de-ponto

Crie e Ative o ambiente virtual:
No Windows:
python -m venv venv
venv\Scripts\activate
No Linux/MacOS:
source venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

Configure o banco de dados:
python manage.py migrate

Popule o banco de dados com dados fictícios:
from ponto_app.models import Empresa, Funcionario, Ponto

Código de criação fornecido no projeto.

Inicie o servidor:
python manage.py runserver

Acessando o Sistema
Abra o navegador em: http://127.0.0.1:8000

📚 Funcionalidades em Detalhes
Página de Registro de Batidas
Filtros: Nome do funcionário e data.
Colunas exibidas:
- Nome do funcionário
- Data
- Horários de entrada e saída
- Horas trabalhadas (calculadas automaticamente)

Estilização
- Layout responsivo e visual limpo.
- CSS dedicado para cada página.

🛠️ Tecnologias Utilizadas
- Django 5.1.4: Framework principal para o desenvolvimento.
- SQLite: Banco de dados simples e eficiente.
- HTML/CSS: Para a interface do usuário.

📂 Banco de Dados
Estrutura dos Modelos

Empresa
- nome: Texto – Nome da empresa.
- endereco: Texto – Endereço da empresa.

Funcionário
- nome: Texto – Nome do funcionário.
- email: Texto – E-mail do funcionário.
- empresa: Relacional – Empresa associada.

Ponto
- funcionario: Relacional – Funcionário associado ao registro.
- data: Data – Data da batida.
- entrada: Hora – Horário de entrada.
- saida: Hora – Horário de saída (opcional).

📄 Licença
Este projeto é open-source e está sob a licença MIT.

💡 Ideias Futuras
- Exportação de relatórios em PDF/Excel.
- Integração com APIs de terceiros.
- Sistema de autenticação para gerentes e administradores.

Contribuições são bem-vindas! 😄

