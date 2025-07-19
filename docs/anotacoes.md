# TODO: Baixar arquivos que é mostrado na aula, está no repositorio
- Qual Versão Python Utilizar - Recomendável a mais recente, porém só aceitavel descer a versão, se alguma biblioteca utilizada, aceitar somente versões anteriores

- Comando ``pyenv local "numero da versão"``

- Próximo passo é executar o comando - ``poetry config virtualenvs.in-project true``

- Comando ``poetry init``

- Comando ``poetry env use "numero da versão"``

- Comando ``poetry shell``

- Comando ``git init``

- Crie o arquivo ``.gitignore``, podendo pesquisar em [toptal git ignore](https://www.toptal.com/developers/gitignore)

- Crie o repositório no github, gitlab ou bitbucket

- Adicione o ``pytest``

- Pesquise sobre a pep 8

- Adicione o ``isort``

- Adicione o ``blue``

- Comando ``isort .``

- Comando ``blue .``

- Adicione o comando abaixo no ``pyproject.toml``:
```bash
    [tool.isort]
    profile = "black"
    know_third_party = []
```

- Uma opção alternativa ao `blue` é o ``flake8``

- Adicione o ``pydocstyle``

- Comando ``pydocstyle .``

- Adicione o ``pip-audit``

- Comando ``pip-audit``

- Adicione o ``taskipy``

- Adicione as tasks ao arquivo ``pyproject.toml``

- Adicione o ``mkdocs``

- Comando ``mkdocs new .``

- Comando ``mkdocs serv``

- Adicione ``poetry add mkdocs mkdocstrings-python pygments mkdocs-material pymdown-extensions``

- Adicionar o mkdocs ao github page
    mkdocs serve
    Adicione ao pyproject
    ```bash
    [tool.poetry.scripts]
    docs-deploy = "mkdocs.__main__:cli"
    ```
    - Adicione ``poetry add mkdocs-git-revision-date-localized-plugin mkdocs-material --group dev``
    Execute o comando ``mkdocs gh-deploy --clean``

- Adicione ``mkdocs-mermaid2-plugin``

- Documentação mermaid [documentação](https://mermaid.js.org/intro/)

- Adicione o ``pre-commit``

- Comando ``pre-commit migrate-config``

- Comando ``poetry add mypy types-setuptools``

- Adicione ``poetry add pandas-stubs``

- Comandos:
    poetry add --group dev pre-commit
    pre-commit clean
    pre-commit install
    pre-commit run --all-files

- Usando ci, crie uma pasta com o nome ``.github`` após isso uma pasta com o nome ``workflow`` e um arquivo com o nome ``ci.yml``. Para pesquisar o que é possivel fazer com o github actions, pesquise em [github actions](https://github.com/features/actions?locale=pt-BR)
