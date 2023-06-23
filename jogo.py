#Substitua o comando while pelo comando for.
#● Escolha um número secreto entre 0 e 100.
#● Crie um nível de dificuldade para o jogo. Peça para o usuário escolher em 
#qual nível ele deseja jogar. O nível é mensurado de acordo com as 
#tentativas.
#● Acrescente um sistema de pontuação. O jogador deve começar com 1000 
#pontos e cada chute errado deve ser subtraído do total de pontos um valor 
#que corresponde a diferença entre o chute e o número secreto. (dica, 
#pesquise sobre a função abs(), ela pode ser útil

import random

numero_secreto = random.randrange(0, 101)
max_tentativas = 0

print("Qual o nivel de dificuldade?")
print("1 - fácil, 2 - Medio, 3 - Dificil!")
nivel = int(input("Digite o nivel:"))

if nivel == 1:
   max_tentativas = 20
elif nivel == 2:
    max_tentativas = 10
elif  nivel == 3:
    max_tentativas = 5

for rodada in range(1, max_tentativas + 1):
    print(f"Tentativas {rodada} de {max_tentativas}")
    valor_escolhido_str = input("Digite um numero entre 1 a 100:")
    print("Você digitou", valor_escolhido_str)
    valor_escolhido = int(valor_escolhido_str)

    if  valor_escolhido < 1  or valor_escolhido > 100:
        print("Numero invalido. o numero deve ser entre 1 e 100")
        continue
    
    acertou  = valor_escolhido == numero_secreto
    maior = valor_escolhido > numero_secreto
    menor = valor_escolhido < numero_secreto

    if acertou:
        print("Parabéns vc acertou o numero secreto") 
        break
    else:
        if maior :
            print("Você errou, o numero escolhido foi maior que o numero secreto")
        elif menor:
            print("Você errou, o numero escolhido foi menor que o numero secreto")

print("Fim de jogo")        