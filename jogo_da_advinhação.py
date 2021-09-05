#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
import os
n = randint(1, 10)
cont = 1
print(10*'-=-')
print('{:^30}'.format("JOGO DA ADIVINHAÇÃO"))
print(10*'-=-')
na = int(input('Digite um número inteiro e veja se acertou:  '))
while na != n:  
  os.system("clear")
  print('{} tentativas'.format(cont))
  print(10*'-=-')
  print('{:^30}'.format("JOGO DA ADIVINHAÇÃO"))
  print(10*'-=-')
  na = int(input('Você errou!! Tente novamente: '))
  cont = cont + 1
os.system("clear")
print('PARABÉNS VOCÊ ACERTOU!!!')
print('Usando {} tentativas'.format(cont))
print('Número do computador: {}'.format(n))
print('Seu número: {} '.format(na))