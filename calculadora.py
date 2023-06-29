#Exercicios calculadora aula06
#Crie uma função calculadora() que receba dois números
#e retorne o resultado das 4 operações básicas da matemática entre eles.


def calculadora(n1, n2):
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2
    return soma, subtracao, multiplicacao, divisao
resultado = calculadora(10, 5)
print(resultado)

#Crie uma função divisão(), que receba dois números como parâmetros 
# e retorne o resultado da divisão do primeiro pelo segundo.

def divisao(num1, num2):
    resultado = num1 / num2
    return resultado
resultado_divisao = divisao(10, 5)
print(resultado_divisao)

