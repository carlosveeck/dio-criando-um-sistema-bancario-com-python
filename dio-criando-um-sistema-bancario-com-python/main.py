menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito realizado com sucesso. Novo saldo: R${saldo:.2f}")
        else:
            print("Valor inválido, operação cancelada.")



    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
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





    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if len(extrato) >= 1:
            for item in extrato:
                print(item)
        else:
            print("Nenhuma movimentação registrada.")
        print(f"\nSaldo atual: R${saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Encerrando o sistema.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")





