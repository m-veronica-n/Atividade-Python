dias = ["nda", "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado"]

num = int(input("Insira um numero de 1  a 7: "))
    
if(num > 7 or num < 1):
    print("Invalido")
else:
    print(dias[num])