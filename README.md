# Controle de Gastos

Programa em Python puro para registrar gastos pessoais e ver quanto foi gasto no total e em cada categoria. Projeto de estudo, feito para praticar lógica de programação e estruturas de dados.

## O que o programa faz

- Guarda uma lista de gastos, cada um com valor, descrição e categoria
- Lista todos os gastos com o valor formatado em reais (duas casas decimais)
- Calcula o total gasto no mês
- Calcula o total gasto em cada categoria

## Como executar

1. Python 3 instalado
2. Clonar o repositório:
   ```
   git clone https://github.com/PauloMellog/controle-gastos.git
   ```
3. Entre na pasta e rode o programa:
   ```
   cd controle-gastos
   python gastos.py
   ```

## Exemplo de saída

```
=== Gastos ===
Farmácia: Saúde R$ 70.00
Mercado: Alimentação R$ 56.50
Shopping: Lazer R$ 115.20

=== Soma total no mês ===
A soma do mês é igual a R$241.70

Saúde: R$ 70.00
Alimentação: R$ 56.50
Lazer: R$ 115.20
```

## Próximos passos

- Organizar o código em funções
- Criar um menu interativo no terminal, com `input()` e `while`
- Validar a entrada do usuário com `try/except`
- Migrar o armazenamento para um banco SQLite e fazer as consultas em SQL

## Sobre os dados

Todos os gastos de exemplo são fictícios.
