# Faça um Programa que leia três números e mostre o maior deles.

primeiro = int(input('primeiro numero: '))
segundo  = int(input('segundo numero : '))
terceiro = int(input('terceiro numero: '))

maior = primeiro
if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro
print('Maior numero: ',maior)