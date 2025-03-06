#Receber uma string e verificar se o inverso da string é igual a ela mesma


def palindromo(palavra):
    if palavra == palavra[::-1]:
        mensagem = "A palavra é um palíndromo."
    else:
        mensagem = "A palavra não é um palíndromo."
    return mensagem

palavra = input("Digite uma palavra: ")
print(palindromo(palavra))

