# Guia Completo para Estruturação de Projetos em Python

Este guia detalhado fornece um passo a passo para configurar um projeto em Python com ferramentas modernas, garantindo organização, qualidade de código, documentação e automação. Ele é baseado em boas práticas e ferramentas amplamente utilizadas na comunidade Python.

## Índice
1. [Configuração do Ambiente Python](#configuração-do-ambiente-python)
2. [Inicialização do Projeto](#inicialização-do-projeto)
3. [Controle de Versão com Git](#controle-de-versão-com-git)
4. [Adição de Dependências e Ferramentas de Desenvolvimento](#adição-de-dependências-e-ferramentas-de-desenvolvimento)
5. [Testes com Pytest](#testes-com-pytest)
6. [Estilo e Linting de Código](#estilo-e-linting-de-código)
7. [Documentação com MkDocs](#documentação-com-mkdocs)
8. [Automação de Tarefas com Taskipy](#automação-de-tarefas-com-taskipy)
9. [Hooks de Pré-Commit](#hooks-de-pré-commit)
10. [Verificação de Tipagem Estática com Mypy](#verificação-de-tipagem-estática-com-mypy)
11. [Integração Contínua com GitHub Actions](#integração-contínua-com-github-actions)

## Configuração do Ambiente Python

### Escolha e Configuração da Versão do Python
- **Escolha da Versão**: Utilize a versão mais recente do Python disponível em [python.org](https://www.python.org/downloads/) para aproveitar novos recursos e atualizações de segurança. Caso bibliotecas específicas exijam uma versão anterior, selecione a versão compatível.
- **Gerenciamento com pyenv**: Use o [pyenv](https://github.com/pyenv/pyenv) para gerenciar múltiplas versões do Python. Configure a versão local do projeto com:
  ```bash
  pyenv local <versão>
  ```
  Exemplo: `pyenv local 3.11.4`

### Configuração do Poetry para Ambientes Virtuais
- O [Poetry](https://python-poetry.org/) é uma ferramenta poderosa para gerenciamento de dependências e ambientes virtuais.
- Configure o Poetry para criar ambientes virtuais dentro do diretório do projeto, garantindo isolamento:
  ```bash
  poetry config virtualenvs.in-project true
  ```

## Inicialização do Projeto

### Inicialização com Poetry
- Crie um arquivo `pyproject.toml` para gerenciar dependências e metadados do projeto:
  ```bash
  poetry init
  ```
- Siga os prompts interativos para configurar detalhes como nome, versão e descrição do projeto.

### Definição da Versão do Python no Poetry
- Especifique a versão do Python para o ambiente virtual, garantindo consistência com o `pyenv`:
  ```bash
  poetry env use <versão>
  ```
  Exemplo: `poetry env use 3.11.4`

### Ativação do Ambiente Virtual
- Ative o ambiente virtual para trabalhar no projeto:
  ```bash
  poetry shell
  ```
- Alternativamente, execute comandos no ambiente virtual sem ativá-lo:
  ```bash
  poetry run <comando>
  ```

## Controle de Versão com Git

### Inicialização do Repositório Git
- Inicialize um repositório Git local:
  ```bash
  git init
  ```

### Criação do Arquivo .gitignore
- Crie um arquivo `.gitignore` para evitar o versionamento de arquivos desnecessários, como ambientes virtuais e caches.
- Utilize o [Toptal's Gitignore Generator](https://www.toptal.com/developers/gitignore) para criar um arquivo adequado para projetos Python.

### Criação do Repositório Remoto
- Crie um repositório em plataformas como [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/) ou [Bitbucket](https://bitbucket.org/).
- Conecte o repositório local ao remoto:
  ```bash
  git remote add origin <url-do-repositório>
  git push -u origin main
  ```

## Adição de Dependências e Ferramentas de Desenvolvimento
- Adicione dependências principais com:
  ```bash
  poetry add <pacote>
  ```
- Adicione dependências de desenvolvimento (usadas apenas em desenvolvimento):
  ```bash
  poetry add --group dev <pacote>
  ```

## Testes com Pytest
- Adicione o [Pytest](https://docs.pytest.org/) para testes automatizados:
  ```bash
  poetry add --group dev pytest
  ```
- Crie testes no diretório `tests/`.
- Execute os testes:
  ```bash
  poetry run pytest
  ```

## Estilo e Linting de Código

### Adesão à PEP 8
- Siga as diretrizes da [PEP 8](https://www.python.org/dev/peps/pep-0008/) para escrever código Python legível e consistente.

### Organização de Imports com isort
- Adicione o [isort](https://pycqa.github.io/isort/) para organizar imports:
  ```bash
  poetry add --group dev isort
  ```
- Execute o isort em todo o projeto:
  ```bash
  isort .
  ```

### Formatação de Código com Black
- Adicione o [Black](https://black.readthedocs.io/en/stable/) para formatação automática de código:
  ```bash
  poetry add --group dev black
  ```
- Execute o Black:
  ```bash
  black .
  ```

### Configuração de isort e Black
- Configure o isort para compatibilidade com o Black no `pyproject.toml`:
  ```toml
  [tool.isort]
  profile = "black"
  ```

### Linting com Flake8 (Opcional)
- Adicione o [Flake8](https://flake8.pycqa.org/en/latest/) para verificação de estilo e erros:
  ```bash
  poetry add --group dev flake8
  ```
- Execute o Flake8:
  ```bash
  flake8 .
  ```

### Verificação de Docstrings com pydocstyle
- Adicione o [pydocstyle](http://www.pydocstyle.org/en/stable/) para verificar convenções de docstrings (PEP 257):
  ```bash
  poetry add --group dev pydocstyle
  ```
- Execute o pydocstyle:
  ```bash
  pydocstyle .
  ```

### Verificação de Vulnerabilidades com pip-audit
- Adicione o [pip-audit](https://github.com/trailofbits/pip-audit) para verificar vulnerabilidades nas dependências:
  ```bash
  poetry add --group dev pip-audit
  ```
- Execute o pip-audit:
  ```bash
  pip-audit
  ```

## Documentação com MkDocs

### Inicialização do MkDocs
- Crie um projeto de documentação com [MkDocs](https://www.mkdocs.org/):
  ```bash
  mkdocs new .
  ```

### Iniciar o Servidor de Desenvolvimento
- Visualize a documentação localmente:
  ```bash
  mkdocs serve
  ```

### Adição de Plugins e Temas do MkDocs
- Adicione pacotes para melhorar a documentação:
  ```bash
  poetry add --group dev mkdocs mkdocstrings mkdocs-material pymdown-extensions
  ```
- Configure o `mkdocs.yml` conforme necessário.

### Implantação no GitHub Pages
- Implante a documentação no GitHub Pages:
  ```bash
  mkdocs gh-deploy
  ```

### Adição do Plugin Mermaid
- Adicione o [mkdocs-mermaid2-plugin](https://github.com/fralau/mkdocs-mermaid2-plugin) para diagramas:
  ```bash
  poetry add --group dev mkdocs-mermaid2-plugin
  ```
- Configure no `mkdocs.yml`:
  ```yaml
  plugins:
    - mermaid2
  ```
- Consulte a [documentação do Mermaid](https://mermaid.js.org/) para criar diagramas.

## Automação de Tarefas com Taskipy
- Adicione o [taskipy](https://github.com/illBeRoy/taskipy) para automatizar tarefas:
  ```bash
  poetry add --group dev taskipy
  ```
- Defina tarefas no `pyproject.toml`:
  ```toml
  [tool.taskipy.tasks]
  test = "pytest"
  lint = "flake8 ."
  format = "black ."
  ```
- Execute tarefas:
  ```bash
  poetry run taskipy test
  ```

## Hooks de Pré-Commit
- Adicione o [pre-commit](https://pre-commit.com/) para verificações automáticas antes de commits:
  ```bash
  poetry add --group dev pre-commit
  ```
- Crie um arquivo `.pre-commit-config.yaml` com os hooks desejados.
- Instale os hooks:
  ```bash
  pre-commit install
  ```
- Execute os hooks em todos os arquivos:
  ```bash
  pre-commit run --all-files
  ```

## Verificação de Tipagem Estática com Mypy
- Adicione o [mypy](http://mypy-lang.org/) para verificação de tipagem estática:
  ```bash
  poetry add --group dev mypy
  ```
- Adicione stubs de tipagem, se necessário (exemplo para Pandas):
  ```bash
  poetry add --group dev pandas-stubs
  ```
- Configure o mypy no `pyproject.toml`.

## Integração Contínua com GitHub Actions
- Crie um arquivo `.github/workflows/ci.yml` para definir pipelines de integração contínua.
- Inclua etapas para instalar dependências, executar testes, linting, etc.
- Consulte a [documentação do GitHub Actions](https://docs.github.com/pt/actions) para mais detalhes.

## Tabela de Ferramentas
| Ferramenta            | Finalidade                              | Comando de Instalação                     | Comando de Execução       |
|-----------------------|-----------------------------------------|-------------------------------------------|---------------------------|
| pyenv                 | Gerenciamento de versões do Python       | -                                         | `pyenv local <versão>`    |
| Poetry                | Gerenciamento de dependências            | -                                         | `poetry init`             |
| Pytest                | Testes automatizados                    | `poetry add --group dev pytest`           | `poetry run pytest`       |
| isort                 | Organização de imports                  | `poetry add --group dev isort`            | `isort .`                 |
| Black                 | Formatação de código                    | `poetry add --group dev black`            | `black .`                 |
| Flake8                | Linting de código                       | `poetry add --group dev flake8`           | `flake8 .`                |
| pydocstyle            | Verificação de docstrings               | `poetry add --group dev pydocstyle`       | `pydocstyle .`            |
| pip-audit             | Verificação de vulnerabilidades          | `poetry add --group dev pip-audit`        | `pip-audit`               |
| taskipy               | Automação de tarefas                    | `poetry add --group dev taskipy`          | `poetry run taskipy <tarefa>` |
| MkDocs                | Documentação                            | `poetry add --group dev mkdocs`           | `mkdocs serve`            |
| mkdocs-mermaid2-plugin| Diagramas na documentação               | `poetry add --group dev mkdocs-mermaid2-plugin` | -                   |
| pre-commit            | Hooks de pré-commit                     | `poetry add --group dev pre-commit`       | `pre-commit run --all-files` |
| mypy                  | Verificação de tipagem estática         | `poetry add --group dev mypy`             | -                         |
