📌 Descrição do Problema Real
Milhões de brasileiros enfrentam dificuldades para controlar seus gastos pessoais. A falta de organização financeira leva ao endividamento, ao consumo impulsivo e à incapacidade de poupar. 
Ferramentas existentes muitas vezes são complexas, pagas ou exigem integração bancária. O resultado é que a maioria das pessoas abandona o controle financeiro por falta de uma solução simples e acessível.

💡 Proposta da Solução
O DeuGreen é uma aplicação web leve, desenvolvida com Python e Django, que permite ao usuário registrar, categorizar, visualizar e excluir seus gastos pessoais de forma rápida e intuitiva. Sem cadastro complicado, sem integrações externas — apenas controle financeiro direto e funcional.

👥 Público-Alvo

Estudantes universitários que precisam controlar mesada ou renda própria
Jovens adultos iniciando sua vida financeira independente
Microempreendedores que precisam separar gastos pessoais dos profissionais
Qualquer pessoa que queira ter clareza sobre para onde vai seu dinheiro


✅ Funcionalidades Principais

Cadastrar um gasto com: descrição, valor, categoria e data
Listar todos os gastos registrados
Filtrar gastos por categoria
Visualizar o total gasto por período ou categoria
Excluir um gasto
Interface web responsiva via Django com templates HTML


🛠️ Tecnologias Utilizadas
TecnologiaFinalidadePython 3.11+Linguagem principalDjango 5.xFramework web (MVC/MTV)SQLiteBanco de dados local (padrão Django)RuffLinting e análise estáticaPytest + pytest-djangoTestes automatizadosGitHub ActionsPipeline de CI


⚙️ Instalação
Pré-requisitos

Python 3.11 ou superior instalado
pip disponível no terminal
Git instalado

Passo a passo
bash# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/financafacil.git
cd financafacil

# 2. Crie e ative o ambiente virtual
python -m venv venv

# No Linux/macOS:
source venv/bin/activate

# No Windows:
venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Aplique as migrações do banco de dados
python manage.py migrate

# 5. (Opcional) Crie um superusuário para acessar o admin
python manage.py createsuperuser

▶️ Execução
bash# Com o ambiente virtual ativado, rode o servidor local
python manage.py runserver
Acesse no navegador: http://127.0.0.1:8000

O painel administrativo do Django está disponível em: http://127.0.0.1:8000/admin


🧪 Rodando os Testes
bash# Execute todos os testes automatizados com pytest
pytest

# Para ver cobertura de código (se pytest-cov estiver instalado)
pytest --cov=core --cov-report=term-missing
Os testes estão localizados na pasta tests/ e cobrem:

Criação válida de um gasto (test_models.py)
Rejeição de valor negativo (test_models.py)
Listagem de gastos via view (test_views.py)
Validação de formulário com dados inválidos (test_forms.py)


🔍 Rodando o Lint (Análise Estática)
Este projeto usa o Ruff para análise estática e padronização de código.
bash# Verificar problemas de estilo e qualidade
ruff check .

# Corrigir automaticamente os problemas corrigíveis
ruff check . --fix
A configuração do Ruff está declarada no pyproject.toml.

🔄 Pipeline de CI (GitHub Actions)
A cada push ou pull request na branch main, o GitHub Actions executa automaticamente:

Configuração do ambiente Python
Instalação das dependências
Execução do lint com Ruff
Execução dos testes com Pytest

O arquivo de configuração está em .github/workflows/ci.yml.
O status atual da pipeline pode ser verificado pelo badge no topo deste README.

📦 Versão
1.0.0 — Versão inicial com funcionalidades básicas de cadastro, listagem, filtragem e exclusão de gastos.
O versionamento segue o padrão Semantic Versioning (SemVer):

MAJOR — mudanças incompatíveis com versões anteriores
MINOR — novas funcionalidades retrocompatíveis
PATCH — correções de bugs

A versão está declarada no pyproject.toml.

📋 Dependências
Todas as dependências estão listadas em requirements.txt e pyproject.toml.
Principais:
django>=5.0
pytest>=8.0
pytest-django>=4.8
ruff>=0.4

👤 Autor
Rafael Carvalho Gonçalves da Silva
Disciplina: Bootcamp II
🔗 Repositório: https://github.com/Raduzinho914/Bootcamp-etapa-inicial-GerenciadordeGastos-.git
