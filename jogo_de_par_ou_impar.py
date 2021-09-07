#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

#Biblioteca para gerar números aleatórios e limpar a tela
from random import randint
import os

#inicio da variavel de controle
acerto = 0

while True:

  #Esse while interno serve para manter o loop até o usuário digitar P ou I
  while True :
    #testa e armazena se sua escolha é par ou impar
    escolha = str(input('Você quer PAR OU IMPAR? [P/I]: ')).upper()
    if escolha == 'P':
      escolha = int(0)
      break
    elif escolha == 'I':
      escolha = int(1)
      break
        
  #Aqui onde a máquina gera sua jogada 
  user = int(input('Digite um número: '))
  pc = randint(1, 10)
  res = (user+pc)%2

  #limpa a tela
  os.system('clear')
  
  #Resultado
  print(27*'=')
  print(' |Máquina = {} | Você = {} |'.format(pc, user))
  print(27*'=')
  print('O total deu {}'.format(user+pc))
  
  #testa se o usuário ganhou
  if escolha == res:
    print('Parabéns! Você ganhou!')
    acerto += 1 
  else: 
    #para o programa
    print('Triste :( Você Perdeu!')
    break
print('Fim de Jogo! Você venceu {} vezes!'.format(acerto))
