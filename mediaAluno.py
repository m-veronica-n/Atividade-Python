# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.


notaOne = float(input("Digite a primeira nota do aluno: "))
notaTwo = float(input("Digite a segunda nota do aluno: "))

media = (notaOne + notaTwo) / 2

if (media >= 7 ):
    print("Aprovado")
elif (media >= 10):
    print("Aprovado com Distinção")
else:
    print("Reprovado")