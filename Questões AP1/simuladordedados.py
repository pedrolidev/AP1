import random

def roll_dice(tamanho_dado, numero_dados):
    soma_resultados = 0
    for _ in range(numero_dados):
        resultado = random.randint(1, tamanho_dado)
        soma_resultados += resultado
    return soma_resultados

def obter_numero_inteiro(mensagem, mensagem_erro=None, valor_minimo=None):
    while True:
        entrada = input(mensagem)
        if entrada == "":
            if valor_minimo is not None and valor_minimo > 0:
                print(f"O número passado deve ser maior que {valor_minimo}!")
            else:
                return None
        elif not entrada.isdigit():
            if mensagem_erro:
                print(mensagem_erro)
            else:
                print("A informação passada não é válida!")
        else:
            numero = int(entrada)
            if valor_minimo is not None and numero < valor_minimo:
                if valor_minimo == 0:
                    print("O número passado deve ser maior que zero!")
                else:
                    print(f"O número passado deve ser maior que {valor_minimo}!")
            else:
                return numero

def main():
    continuar = True

    while continuar:
        tamanho_dado = obter_numero_inteiro("Forneça o tamanho do dado que será rolado (ENTER para sair): ", "A informação passada não é válida!", valor_minimo=0)

        if tamanho_dado is None:
            continuar = False
        else:
            numero_dados = obter_numero_inteiro("Forneça o número de dados que serão rolados (em branco == 1): ", "A informação passada não é válida!", valor_minimo=0)

            if numero_dados is None:
                continuar = False
            elif numero_dados == 0:
                print("O número passado deve ser maior que zero!")
            else:
                resultado = roll_dice(tamanho_dado, numero_dados)
                print(f"\nResultado do lançamento de {numero_dados} dado(s) de {tamanho_dado} lados: {resultado}")

if __name__ == "__main__":
    main()