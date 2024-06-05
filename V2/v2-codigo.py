import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor > 0 and valor <= limite:
        excedeu_saldo = valor > saldo
        excedeu_numero_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print(f"Valor selecionado excedeu seu saldo atual de R${saldo:.2f}. Operação cancelada.")
        elif excedeu_numero_saques:
            print(f"Você já atingiu o número diário de saques, tente novamente dentro de 24h.")
        else:
            saldo -= valor
            extrato.append(f"Saque: R${valor:.2f}")
            numero_saques += 1
            print(f"Saque realizado com sucesso. Novo saldo: R${saldo:.2f}")
    else:
        print(f"Insira um valor válido. Limite atual de saque: R${limite:.2f}.")

    return saldo, extrato


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")
        print(f"Depósito realizado com sucesso. Novo saldo: R${saldo:.2f}")
    else:
        print("Valor inválido, operação cancelada.")
    return saldo, extrato


def gerar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if len(extrato) >= 1:
        for item in extrato:
            print(item)
    else:
        print("Nenhuma movimentação registrada.")
    print(f"\nSaldo atual: R${saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF do usuário")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    nome = input("Informe o nome do usuário: ")
    data = input("Informe o data de nascimento do usuário (dd/mm/aaaa)")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data, "cpf": cpf, "endereco": endereco})
    return usuarios

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    numero_saques = 0
    usuarios = []
    contas = []
    extrato = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor que deseja depositar: "))
            saldo, extrato = deposito(saldo, valor, extrato)


        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(saldo=saldo,
                                   valor=valor,
                                   extrato=extrato,
                                   limite=limite,
                                   numero_saques=numero_saques,
                                   LIMITE_SAQUES=LIMITE_SAQUES)


        elif opcao == "e":
            gerar_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Encerrando o sistema.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
