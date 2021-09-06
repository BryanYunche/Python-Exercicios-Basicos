#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele diser que quer mostrar 0 termos.
#an = a1 + (n – 1).r
print(5*'-=-')
print('Gerador de PA')
print(5*'-=-')
print('teste de pa\n')
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
an = int(input('Digite até qual termo da PA você quer ver: '))
#c é a variavél de controle do segundo while
c = 0
mterm = 1
while mterm != 0:
  # Segundo while
  while c < an:
    c += 1
    #Aqui o c tem o papel de ser o controlador de termos da PA
    pa = a1+(c-1)*r
    print(' {} ->'.format(pa), end='')
  print(' PAUSA')
  mterm = int(input('Quantos termos mais você quer ver? '))
  #an recebe o ultimo valor de termo mais quantos termos o usuário quer ver
  an = c + mterm
print('{} termos foram vistos!'.format(an))
print('Fim do Programa!')
