numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja realizar:\n[+, -, /, *] : ")


def analise():
    if (resultado // 1 == resultado):
        print("Valor Inteiro")
        if resultado % 2 == 0:
            print("Valor Par")
            if resultado > 0:
                print("Valor Positivo")
            else:
                print("Valor Negativo")
        else:
            print("Valor Impar")
    else:
        print("Valor Decimal")


if operacao == '+':
    resultado = numero1 + numero2
    print("Resultado: ", resultado)
    analise()
elif operacao == '-':
    resultado = numero1 - numero2
    print("Resultado: ", resultado)
    analise()
elif operacao == '/':
    resultado = numero1 / numero2
    print("Resultado: ", resultado)
    analise()
elif operacao == '*':
    resultado = numero1 * numero2
    print("Resultado: ", resultado)
    analise()
else:
    print("Valor Invalido")