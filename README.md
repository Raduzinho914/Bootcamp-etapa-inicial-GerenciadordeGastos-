# DeuGreen — Gerenciador de Gastos Pessoais

![CI](https://github.com/Raduzinho914/Bootcamp-etapa-inicial-GerenciadordeGastos-/actions/workflows/ci.yml/badge.svg)

---

## Descrição do Problema

Milhões de brasileiros enfrentam dificuldades para controlar seus gastos pessoais. A falta de organização financeira leva ao endividamento, ao consumo impulsivo e à incapacidade de poupar.
Ferramentas existentes muitas vezes são complexas, pagas ou exigem integração bancária. O resultado é que a maioria das pessoas abandona o controle financeiro por falta de uma solução simples e acessível.

---

## Proposta de Solução

O **DeuGreen** é uma aplicação web leve, desenvolvida com Python e Django, que permite ao usuário registrar, categorizar, visualizar e excluir seus gastos pessoais de forma rápida e intuitiva. Sem cadastro complicado, sem integrações externas — apenas controle financeiro direto e funcional.

---

## Público-Alvo

- Estudantes universitários que precisam controlar mesada ou renda própria
- Jovens adultos iniciando sua vida financeira independente
- Microempreendedores que precisam separar gastos pessoais dos profissionais
- Qualquer pessoa que queira ter clareza sobre para onde vai seu dinheiro

---

## Funcionalidades

- Listar todos os gastos registrados
- Adicionar um gasto com: descrição, valor, categoria e data
- Editar um gasto existente
- Excluir um gasto
- Filtrar gastos por categoria
- Visualizar o total gasto por período ou categoria

---

## Tecnologias Utilizadas

- Python 3.11+
- Django 5.x
- SQLite
- pytest / pytest-django
- ruff
- GitHub Actions

---

## Instalação

```bash
# Clone o repositório
git clone https://github.com/Raduzinho914/Bootcamp-etapa-inicial-GerenciadordeGastos-.git
cd Bootcamp-etapa-inicial-GerenciadordeGastos-

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate
```

---

## Execução

```bash
python manage.py runserver
```

Acesse no navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

> Painel administrativo disponível em: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## Rodando os Testes

```bash
pytest
```

Os testes estão localizados na pasta `tests/` e cobrem:

- Criação válida de um gasto (`test_models.py`)
- Rejeição de valor negativo (`test_models.py`)
- Listagem de gastos via view (`test_views.py`)
- Validação de formulário com dados inválidos (`test_forms.py`)

---

## Rodando o Lint

```bash
ruff check .
```

A configuração do Ruff está declarada no `pyproject.toml`.



## Versão

**1.0.0** — Versão inicial com funcionalidades básicas de cadastro, listagem, filtragem e exclusão de gastos.

Versionamento seguindo o padrão [SemVer](https://semver.org/):

- `MAJOR` — mudanças incompatíveis com versões anteriores
- `MINOR` — novas funcionalidades retrocompatíveis
- `PATCH` — correções de bugs

---

## Dependências

```
django>=5.0
pytest>=8.0
pytest-django>=4.8
ruff>=0.4
```

Todas as dependências estão listadas em `requirements.txt` e `pyproject.toml`.

---

## Autor

**Rafael Carvalho Gonçalves da Silva**  
Disciplina: Bootcamp II  
🔗 Repositório: https://github.com/Raduzinho914/Bootcamp-etapa-inicial-GerenciadordeGastos-.git