#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print(20*'=')
print('{:^20}'.format('BRYANs BANK'))
print(20*'=')

#Entrada de dados
saque  = int(input('\nDigite quantos R$ deseja sacar: '))

#Estetica
print(20*'=')

#Iniciar variaveis
resto1 = resto2 = resto3 = n20 = n10 = n1 = 0

#Processamento
n50 = saque//50
resto1 = saque%50

#Quantas notas de 50
if (resto1 >= 0):
  if (n50 > 0):
    print('Total de {} cedulas de 50'.format(n50))

#Quantas notas de 20
if (resto1 > 0):
  n20 = resto1//20
  resto2 = resto1%20
  if (n20 > 0):
    print('Total de {} cedulas de 20'.format(n20))

#Quantas notas de 10
if (resto2 > 0):
  n10 = resto2//10
  resto3 = resto2%10
  if (n10 > 0):
    print('Total de {} cedulas de 10'.format(n10))

#Quantas notas de 1
if (resto3 > 0):
  n1 = resto3//1
  if (n1 > 0):
    print('Total de {} moedas de 1 real.'.format(n1))

#Estetica
print(20*'=')

