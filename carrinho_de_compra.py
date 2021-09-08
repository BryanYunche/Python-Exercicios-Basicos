#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

#inicio da variavel de soma dos produtos
soma = prod = 0

#Constante
mil = 1000
nome = str(input('Digite o nome do produto: '))
val = float(input('Digite o valor do produto: '))
menor = val
while True:
  #Faz o ususário ter que digitar S ou N
  while True:
    cont = str(input('Deseja continuar? [S/N]: ')).upper()
    if cont == 'N':
      break
    if cont == 'S':
      break

  #termina o programa
  if cont == 'N':
    break
     
  #Entrada de dados    
  nome = str(input('Digite o nome do produto: '))
  val = float(input('Digite o valor do produto: '))
  
  #Soma do preço dos produtos
  soma = soma + val

  #Calcula quantos produtos custa mais que R$1000
  if val > mil:
    prod = prod + 1

  #Nome do menor preço
  if val < menor:
    menor = val
    nomeMenor = nome

print('O total da compra foi: R${}'.format(soma))
print('{} produtos custaram mais de R$1000'.format(prod))
print('O menor produto foi {} que custa R${} .'.format(nomeMenor, menor))