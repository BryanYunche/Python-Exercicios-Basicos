#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Digite um número para ver seu fatorial: '))
controle = 1
fatorial = 1
while controle <= n:
  fatorial = (fatorial*controle)
  controle += 1
n2 = 1
s = ''
while n2 <= n:
  strconv = str(n2)
  s = (s + ' X ' + strconv)
  n2 += 1
print('Calculando {}!: {} : {}'.format(n, s[2:], fatorial))
