# Sistema Bancário 🏦

Este repositório é a continuação do sistema bancário desenvolvido no módulo anterior em Python, com objetivo do aprendizado dos princípios de Programação Orientada a Objetos (POO). O projeto permite gerenciar clientes, contas bancárias, e realizar transações como depósitos, saques e visualização de extratos.


## Funcionalidades

- **Criação de Clientes:** Cadastro de clientes com dados pessoais e endereço.
- **Abertura de Contas Bancárias:** Associadas aos clientes, com controle de saldo e histórico.
- **Depósitos e Saques:** Operações bancárias básicas com verificação de limites.
- **Extrato Bancário:** Listagem das transações realizadas na conta.


## Estrutura do Projeto

O sistema é modularizado com classes que representam entidades reais do contexto bancário:

### Classes

| Classe           | Descrição |
|------------------|-----------|
| `Cliente`        | Representa um cliente do banco, contendo uma lista de contas. |
| `PessoaFisica`   | Subclasse de `Cliente` com nome, CPF e data de nascimento. |
| `Conta`          | Classe base para contas bancárias com saldo, número e agência. |
| `ContaCorrente`  | Subclasse de `Conta` com limites de saque e saldo negativo. |
| `Historico`      | Armazena o histórico de transações de uma conta. |
| `Transacao`      | Classe abstrata para operações bancárias. |
| `Saque`          | Representa uma transação de saque. |
| `Deposito`       | Representa uma transação de depósito. |

### Funções

| Função                      | Finalidade |
|-----------------------------|------------|
| `menu()`                    | Exibe o menu principal. |
| `filtrar_cliente()`         | Busca cliente por CPF. |
| `recuperar_conta_cliente()` | Retorna a conta associada ao cliente. |
| `depositar()`               | Realiza um depósito. |
| `sacar()`                   | Realiza um saque. |
| `exibir_extrato()`          | Mostra o extrato da conta. |
| `criar_cliente()`           | Cria um novo cliente. |
| `criar_conta()`             | Associa uma nova conta ao cliente. |
| `listar_contas()`           | Lista todas as contas cadastradas. |
| `main()`                    | Executa o sistema. |



## Links Importantes

- Bootcamp: [Luizalabs Back-end com Python](https://web.dio.me/track/luizalabs-back-end-com-python)