
#Modifique a função feita em sala velocidade() para que utilize a função divisão 
#para calcular a velocidade

def divisao(num1,num2):
    if num2 != 0:
        div = num1 / num2
        return div
    else:
        return False

def velocidade(distancia,tempo):
    if divisao(distancia,tempo) != False:
        velocidade = divisao(distancia,tempo)
        return velocidade
    else:
        return 'Não é possível dividir por zero'

print(velocidade(100,10))
