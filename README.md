# Bootcamp-DIO-desafio-bancario

## Versão 1:

Repositório para projeto de desafio de código do Bootcamp DIO.

O desafio consiste em criar um sistema bancário simples, seguindo algumas regras iniciais.

1 - O código deve ser em Python.

2 - Limite de saque em 500 reais cada saque, independente do saldo total.

3 - Limite de 3 saques realizados.

4 - O extrato deve apresentar valor no formato 100.00

5 - Não pode haver depósito em valor negativo.

## Versão 2:

Na segunda versão foi adicionado novas funçoes, como criar conta, usuario, e listar contas.

## Versão 3:

### Introdução

Com os novos conhecimentos adquiridos sobre decoradores, geradores e iteradores, você foi encarregado de implementar as seguintes funcionalidades no sistema:
- Decorador de log
- Gerador de relatórios
- Iterador personalizado

#### Decorador de log:

Implemente um decorador que seja aplicado a todas as funções de transações (depósito, saque, criação de conta, etc). Esse decorador deve registrar (printar) a data e hora de cada transação, bem como o tipo de transação.

#### Gerador de relatórios:

Crie um gerador que permita iterar sobre as transações de uma conta e retorne, uma a uma, as transações que foram realizadas. Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos).

#### Iterador personalizado:

Implemente um iterador personalizado ContaIterador que permita iterar sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual, etc).