# CSV para vCard

Este projeto é um simples script em Python que converte um arquivo CSV contendo uma lista de contatos (nomes e telefones/celulares) em um arquivo vCard (.vcf), que pode ser importado diretamente para a agenda de um telefone celular.

## Funcionalidades

- Lê um arquivo CSV com colunas de Nome e Celular.
- Gera um arquivo vCard (.vcf) contendo os contatos.
- Suporta múltiplos contatos no mesmo arquivo CSV.

## Exemplo de Estrutura de Arquivo CSV

O arquivo CSV, deve ter no nome de contatos e ter a seguinte estrutura com cabeçalhos:

```csv
Nome,Celular
João Silva,+5511987654321
Maria Souza,+5511998765432
```