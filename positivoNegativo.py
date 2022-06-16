#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


print("Positivo ou Negativo\n")
numero = int(input("Digite um valor: "))
resto = numero % 2 

if (resto == 0) :
    print("Positivo")
else:
    print("Negativo")
