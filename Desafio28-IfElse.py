from random import randint
from time import sleep
comp = randint(0, 5) # Randomiza um número entre os números escolhidos
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if jogador == comp:
    print('Parabéns! Eu pensei no número {}, você conseguiu me vencer!'.format(comp))
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(comp, jogador))