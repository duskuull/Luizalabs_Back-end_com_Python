# Desafio: Otimizando o Sistema Bancário com Funções Python

## Objetivo Geral
Separar as funcões existentes de saque, depósito e extrato em funcões. Criar duas novas funcões: cadastrar usuário (cliente) e cadastrar conta bancária.


## Desafio

Deixar o código mais modularizado, utilizando funções em Python para as operações existentes: sacar, depositar e visualizar extrato. Para a versão 2 do sistema é necessário criar duas novas funções: criar um novo usuário (cliente do banco) e criar conta uma nova corrente (vincular com usuário).

## Separação em funções

Foi criada funções para todas as operações do sistema. Para exercitar a utilização de def, if, else, elif, while e etc.
Cada função tem uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.

### Saque
A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, número_saques, limite_saques.
Sugestão de retorno: saldo e extrato.

### Depósito
A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato.
Sugestão de retorno: saldo e extrato.

### Extrato
A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

### Novas funções
Foi criada duas novas funções: criar novo usuário e criar nova conta corrente. 

### Criar usuário (cliente)
O programa armazena os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. 
O endereço é uma string com o formato: logradouro, número - bairro - cidade/sigla estado.
São armazenados somente os números do CPF. Não pode ser cadastrados 2 usuários com o mesmo CPF.

### Criar conta corrente
O programa armazena as contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: 0001. O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

#### Link do primeiro desafio: [Criando um sitemap bancário em Python](https://web.dio.me/project/otimizando-o-sistema-bancario-com-funcoes-python/learning/82a55799-cfb8-479d-85a3-4982e29c90ba?back=/track/luizalabs-back-end-com-python&tab=undefined&moduleId=undefined)