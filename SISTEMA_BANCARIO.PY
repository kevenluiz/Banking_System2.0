c = {'limpa': '\033[m',
    'a': '\033[1;34m',
    'ama': '\033[1;33m',
    'lilás': '\033[1;35m',
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'b': '\033[1;30m'}
menu = """ESCOLHAR UMA DAS OPÇÕES ABAIXO:
[ 1 ] DEPOSITAR
[ 2 ] SACAR
[ 3 ] EXTRATO
[ 4 ] SAIR
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input('informe o valor do deposito:'))

        if valor > 0:
            saldo += valor
            extrato += f"deposito R$ :{ valor :.2f}\n"
            print('vc fez um deposito de R$ {:.2f} '.format(valor))
        else:
            print("operação inválida, o valor informado é inválido.")
    elif opcao == "2":
        valor = float(input('informe o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= limite_saques
        if excedeu_saldo:
            print('operação falhou! você não tem saldo suficiente.')
        elif excedeu_limite:
            print('operação falhou! o valor de saque excedeu o limite')
        elif excedeu_saque:
            print('operação falhou! número máximo de saques atingido')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor :.2f}\n'
            numero_saques += 1
        else:
            print('operação falhou! o valor é inválido')

    elif opcao == "3":
        print('°-°-' * 11)
        print('EXTRATO')
        print('não foram realizadas movimentações.'if not extrato else extrato)
        print(f'\n saldo: R$ {saldo:.2f}')
        print('°-°-'*11)
    elif opcao == "4":
        print('OPERAÇÃO FINALIZADA! VOLTE SEMPRE.')
        break
    else:
        print('INFORMAÇÃO INVÁLIDA, TENTE NOVAMENTE.')