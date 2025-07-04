menu = """

SELECIONE A OPÇÃO DESEJADA:
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n================ COMPROVANTE ================")
            print("Não há movimentações a serem detalhadas." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=============================================")

        else:
            print("Valor inválido! Informe um valor válido.")

    elif opcao == "2":
        valor = float(input("Informe um valor para saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação inválida! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação inválida! Valor superior a limite de saque.")

        elif excedeu_saques:
            print("Operação inválida! Limite de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n================ COMPROVANTE ================")
            print("Não há movimentações a serem detalhadas." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=============================================")

        else:
            print("Operação inválida! Informe um valor válido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não há movimentações a serem detalhadas." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
