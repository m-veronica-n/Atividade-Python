numero = int(input('Impute um numero inteiro positivo: '))

unidade = numero % 10

numero = (numero - unidade)/10

dezena = numero % 10
numero = (numero - dezena)/10
centena = numero

dezena = int(dezena)
centena = int(centena)
print(centena,'centena(s),',dezena,'dezena(s) e',unidade,'unidade(s)')