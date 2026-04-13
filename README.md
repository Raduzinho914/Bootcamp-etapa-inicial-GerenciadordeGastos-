# Bootcamp-etapa-inicial-GerenciadordeGastos-

[![CI](https://github.com/seu-usuario/Bootcamp-etapa-inicial-GerenciadordeGastos-/actions/workflows/ci.yml/badge.svg)](https://github.com/seu-usuario/Bootcamp-etapa-inicial-GerenciadordeGastos-/actions/workflows/ci.yml)

## Descrição do Problema

A falta de controle financeiro diário é uma dor que afeta grande parte da população, gerando estresse, falta de previsibilidade e endividamento. O problema ocorre no dia a dia, quando as pessoas perdem o controle dos pequenos gastos por considerarem as planilhas tradicionais complexas ou burocráticas demais para registrar despesas rápidas pelo celular.

## Proposta de Solução

Uma aplicação web simples, rápida e direta ao ponto que permite ao usuário registrar rapidamente o valor, a categoria e a data de uma despesa. Ao focar apenas no essencial, o sistema diminui o atrito do registro e oferece uma visualização clara para onde o dinheiro está indo ao longo do mês.

## Público-alvo

Estudantes universitários, jovens profissionais, microempreendedores e qualquer pessoa que deseje abandonar planilhas complexas e adotar um controle de despesas ágil e simplificado.

## Funcionalidades

* Listar despesas cadastradas ordenadas por data.
* Adicionar novo registro de gasto com valor e descrição.
* Editar informações de um lançamento feito com erro.
* Excluir uma despesa do sistema.
* Filtrar por categoria (ex: Alimentação, Transporte, Lazer).

## Tecnologias Utilizadas

* Python 3.13
* Django 4.2
* SQLite
* pytest / pytest-django
* ruff
* GitHub Actions

## Instalação e Execução

```bash
# Clone o repositório
git clone [https://github.com/seu-usuario/Bootcamp-etapa-inicial-GerenciadordeGastos-.git](https://github.com/seu-usuario/Bootcamp-etapa-inicial-GerenciadordeGastos-.git)
cd Bootcamp-etapa-inicial-GerenciadordeGastos-

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Execução
python manage.py runserver