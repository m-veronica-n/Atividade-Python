#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato
primeiro = float(input('Preco primeiro produto : '))
segundo  = float(input('Preco segundo produto  : '))
terceiro = float(input('Preco terceiro produto : '))

menor = primeiro
if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro
print('Produto com menor preco: ',menor)