#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n1 = 0
prim = [2, 3, 5, 7]
cont = int(input('Digite um número inteiro: '))
if not((cont%2 == 0) or (cont%3 == 0) or (cont%5 == 0) or (cont%7 == 0)) or (cont in prim):
  print('O numero {} é primo pois é divisivel apenas po 1 e por ele mesmo!!'.format(cont))
  for n in range(1, cont+1):
    n1 = n1 + 1
    if (n1 == 1) or (n1 == cont):
      print( '\033[32m', n1, '\033[0;0m' ,end = ' ')
    elif (n1 != 1) or (n1 != cont):
      print( '\033[31m', n1, '\033[0;0m' ,end = ' ')
else:
  print('O número {} não é primo'.format(cont))
print('\nFIM DO PROGRAMA!!!')
