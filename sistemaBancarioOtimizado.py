def depositar(saldo, extrato, /):
    valor = float(input("Insira o valor do deposito: "))

    if valor > 0:
        saldo += valor
        extrato += f'Deposito: R$ {valor:.2f}\n'

    else:
        print("Operação inválida. O valor inserido é inválido.")

    return saldo, extrato


def sacar(*, saldo, extrato, numero_saques, limite, limite_saques):
    valor = float(input("Insira o valor do saque: "))

    if valor > saldo:
        print("Operação inválida. Não há saldo suficiente.")

    elif numero_saques >= limite_saques:
        print("Operação inválida. O número máximo de saques diários foi excedido.")

    elif valor > limite:
        print("Operação inválida. O valor do saque inserido  excede o limite.")

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque R$ {valor:.2f}\n'
        numero_saques += 1

    else:
        print("Operação inválida. O valor inserido é inválido.")

    return saldo, extrato, numero_saques


def extratos(saldo, extrato):
    print(" EXTRATO ".center(27, '#'))
    print(f'Não foram realizadas operações' if not extrato else extrato)
    print(f'Saldo atual: R$ {saldo:.2f}\n')
    print("#".center(27, '#'))


def menu():
    print(f"""
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [nu] Novo usuário
    [nc] Nova conta""")


def criar_usuário(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("""\nConta não criada! Usuário não foi encontrado, Crie um novo
          usuário para criar uma nova conta.""")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        menu()

        opcao = input().lower()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                numero_saques=numero_saques,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            extratos(saldo, extrato=extrato)

        elif opcao == "q":
            print("Saindo...")
            break

        elif opcao == "nu":
            criar_usuário(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)


        else:
            print("Operação inválida. Por favor selecione novamente uma operação.")


main()