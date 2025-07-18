# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Workflow

```mermaid
flowchart LR
    subgraph ETL[Pipeline]
        A(Multiplos Arquivos Excel) --> B[Extract: extract_from_excel]
        B --> C[Gera uma lista de Dataframes]
        C --> D[Gera um Dataframe Consolidado]
        D --> |Salva o consolidado em Excel| E[Pasta Output: Um arquivo único Excel]
    end
```

# Função de transformação de dados
### ::: src.infrastructure.data.pipeline.extract.extract_from_excel
