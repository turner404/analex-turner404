# Projeto Analisador Léxico - Analex

## Pré-requisitos

Para a implementação da fase de Análise Léxica, é necessário instalar algumas ferramentas, como o pytest e a biblioteca para implementação do autômato. Os pré-requisitos podem ser instalados utilizando o arquivo `requirements.txt`.

Para instalar as dependências:
```
pip install -r requirements.txt
```

### Execução de Testes
O projeto contém arquivos de exemplo em C- para testes. Os testes estão localizados no diretório tests, na raiz do projeto.

### Para executar um teste específico:
A implementação do analisador léxico (analex.py) pode ser chamada. O parâmetro -k pode ser utilizado para que somente tokens e chaves de erros sejam impressos:
```
python analex.py -k prog-002.cm
```

### Para executar todos os testes:
Utilize o pytest:
```
pytest -v
```
