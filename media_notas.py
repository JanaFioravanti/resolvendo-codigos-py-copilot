#calcular a média de três notas de um aluno
#Entrada: três notas
#Saída: a média das notas

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a terceira nota: "))
media = (nota01 + nota02 + nota03) / 3
print("A média das notas é: {:.2f}".format(media))