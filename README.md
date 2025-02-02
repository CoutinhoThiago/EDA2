# Bitmap Index: Estrutura, Funcionamento e Algoritmos

## Descrição do Projeto

Este projeto explora a estrutura de dados **Bitmap Index**, que é amplamente utilizada em sistemas de gerenciamento de banco de dados para otimizar consultas em grandes volumes de dados. O Bitmap Index armazena informações em um formato de bits que representam a presença ou ausência de valores específicos em um conjunto de dados, permitindo operações rápidas e eficientes de busca, análise e filtragem de informações.

## Estrutura do Projeto

- **generate_data.py**: Gera dados aleatórios e os salva em um arquivo CSV.
- **bitmap_index.py**: Implementa a estrutura de dados Bitmap Index, incluindo métodos para construção, consulta, compressão e operações de interseção, união e diferença.
- **comparison.py**: Compara o desempenho do Bitmap Index com listas e dicionários em operações de busca, interseção, união e diferença.
- **main.py**: Executa o fluxo principal do projeto, gerando dados, construindo o Bitmap Index e realizando comparações de desempenho.

## Como Executar

1. **Executar código completo**:
```python main.py```

2. **Gerar Dados**:
```python generate_data.py```