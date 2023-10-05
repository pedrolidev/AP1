n1 = int(input("Digite o valor do primeiro número:"))
x = 0

while True:
    n2 = int(input("Digite o valor do segundo número:"))

    print("""[1] soma
[2] subtração
[3] multiplicação
[4] divisão
[ENTER] desistir""")

    e = input("Escolha o que você quer fazer com os valores inseridos:")

    if e == "1":
        nt = n1 + n2
        n1 = nt
        print("O resultado da sua conta é", nt)
        c = input("Deseja continuar com o resultado(c), limpar a conta(X) ou desistir(ENTER)?")
        if c == "x" or c == "X":
            n1 = int(input("Digite o valor do primeiro número:"))

        elif c == "":
            print("Obrigado por tentar!")
            break

    elif e == "2":
        nt = n1 - n2
        n1 = nt
        print("O resultado da sua conta é", nt)
        c = input("Deseja continuar com o resultado(c), limpar a conta(X) ou desistir(ENTER)?")
        if c == "x" or c == "X":
            n1 = int(input("Digite o valor do primeiro número:"))

        elif c == "":
            print("Obrigado por tentar!")
            break

    elif e == "3":
        nt = n1 * n2
        n1 = nt
        print("O resultado da sua conta é", nt)
        c = input("Deseja continuar com o resultado(c), limpar a conta(X) ou desistir(ENTER)?")
        if c == "x" or c == "X":
            n1 = int(input("Digite o valor do primeiro número:"))

        elif c == "":
            print("Obrigado por tentar!")
            break

    elif e == "4":
        nt = n1 / n2
        n1 = nt
        print("O resultado da sua conta é", nt)
        c = input("Deseja continuar com o resultado(c), limpar a conta(X) ou desistir(ENTER)?")
        if c == "x" or c == "X":
            n1 = int(input("Digite o valor do primeiro número:"))

        elif c == "":
            print("Obrigado por tentar!")
            break

    elif e == "":
        print("Obrigado por tentar!")
        break

    else:
        print("ERRO! ERRO! CALCULADORA DESLIGANDO!")
        break