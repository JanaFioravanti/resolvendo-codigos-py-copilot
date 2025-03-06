#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar
#Como saída, imprima "par" ou "ímpar", conforme o caso

num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    mensagem = "par"
else:
    mensagem = "ímpar"
print("O número é", mensagem)

