# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.


salario = float(input("Digite o seu salário : "))

salario_baixo = salario * 0.20
baixo = salario * 1.20

salario_medio = salario * 0.15
medio = salario * 1.15

salario_alto = salario * 0.10
alto = salario * 1.10

salario_muitoAlto = salario * 0.5
muitoAlto = salario * 1.05

print("#------------------------------------#")
print("Salário antes do reajuste : ", salario)

if (salario <= 280):
    print("----Salário Baixo----\n")
    print("Aumento de 20 %\nValor: ", salario_baixo, "Valor com aumento: ", baixo )

elif(salario > 200 and salario <= 700):
    print("----Salário Médio----\n")
    print("Aumento de 15 %\nValor: ", salario_medio, "Valor com aumento: ", medio )

elif(salario > 700 and salario <= 1500):
    print("----Salário Alto----\n")
    print("Aumento de 10 %\nValor: ", salario_alto, "Valor com aumento: ", alto )

else:
       print("----Salário Muito Alto----\n")
       print("Aumento de 5 %\nValor: ", salario_muitoAlto, "Valor com aumento: ", muitoAlto )



