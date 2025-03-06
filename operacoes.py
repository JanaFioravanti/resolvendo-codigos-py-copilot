#solicitar como entrada dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
#solicitar como entrada a operação a ser realizada
operacao = input("Digite a operação desejada (+, -, *, /): ")
#realizar a operação
if operacao == "+":
    operacao_nome = "soma"
    resultado = num1 + num2
elif operacao == "-":
    operacao_nome = "subtração"
    resultado = num1 - num2
elif operacao == "*":
    operacao_nome = "multiplicação"
    resultado = num1 * num2
elif operacao == "/":
    operacao_nome = "divisão"
    resultado = num1 / num2
else:
    resultado = "Operação inválida"
#mostrar o resultado
print("O Resultado da operação", operacao_nome, "é: ", resultado)
#fim do programa    