#Faça um Programa que leia três números e mostre o maior e o menor deles.

primeiro = int(input('primeiro numero: '))
segundo  = int(input('segundo numero : '))
terceiro = int(input('terceiro numero: '))

maior = primeiro
if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro
print('Maior numero: ',maior)

menor = primeiro
if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro
print('Menor numero: ',menor)