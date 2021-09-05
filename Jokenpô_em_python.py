#Jogo JO KEN PÔ em Python
import time
import os
import random
comp = ['Pedra', 'Papel', 'Tesoura']
print('Suas opções:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
escolha = int(input('Escolha sua jogada: '))
os.system ("clear")
if escolha < 3:
  time.sleep(0.5)    
  print('JO')
  time.sleep(0.5)
  print('KEN')
  time.sleep(0.5)
  print('PÔ') 
  os.system("clear")
  seleciona = random.choice(comp)
  print(20*'-=')
  print('Sua escolha foi: {}'.format(comp[escolha]))
  print('A escolha da máquina foi: {}'.format(seleciona))
  print(20*'-=')

  ver = 0
  if seleciona == comp[escolha]:
        print('EMPATE')
        ver = 1
  if ver == 0:
    if comp[0]==seleciona and escolha == 1:
      print('VOCÊ GANHOU!!!')
    elif comp[0]==seleciona and escolha == 2:
      print('VOCÊ PERDEU!!')
    elif comp[1]==seleciona and escolha == 0:
      print('VOCÊ PERDEU!!')
    elif comp[1]==seleciona and escolha == 2:
      print('VOCÊ GANHOU!!')
    elif comp[2]==seleciona and escolha == 0:
      print('VOCÊ GANHOU!!')
    elif comp[2]==seleciona and escolha == 1:
      print('VOCÊ PERDEU!!')
else:
  print('JOGADA INVÁLIDA')
  print('Você só pode digitar [0], [1] e [2]')
print('FIM DE JOGO!')
