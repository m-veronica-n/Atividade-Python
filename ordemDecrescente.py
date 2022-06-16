# Faça um Programa que leia três números e mostre-os em ordem decrescente.


print("Ordem Decrescente de Três números")

one = int(input('Primeiro numero: '))
two  = int(input('Segundo numero : '))
three = int(input('Terceiro numero: '))

print(one,'---',two,'---',three)
if(three > two):
    aux = three
    three = two
    two = aux
if(two > one):
    aux = two
    two = one
    one = aux
if(three > two):
    aux = three
    three = two
    two = aux
print("Ordem Decrescente: \n")
print(one,'---',two,'---',three)