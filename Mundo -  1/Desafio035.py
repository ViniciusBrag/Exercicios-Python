print('=' * 4, 'Desafio ', '=' * 4)

print('Analisando o triangulo e classificando-o!')
print('''Dada as condições para formar se um triângulo: \n| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b \n''')

print('''Dada condições para Triângulo equilátero:
 A = B e B = C e A = C \n''')

print('''Dada condições para Triângulo isósceles:
 (A = B)  (B = C) e (A # B) \n''')


a = float(input('Digite a reta 1: '))
b = float(input('Digite a reta 2: '))
c = float(input('Digite a reta 3: '))
print('\n')

if (a - b) < c < b + c and (a - c) < b < a + c or (b - c) < a < b + c:
    print('''Dados o valor de cada lado seja: \n reta 1: {:.0f} \n reta 2: {:.0f} \n reta 3: {:.0f}
Seguindo a regra da existência dos triângulos é possivel formar-se um triângulo! \n '''.format(a, b, c))
else:
    print('Os valor informados não pode formar-se um triângulo devido a regra de existência de um triângulo \n ')

if a == b and b == c or a == c:
    print('''Dada as condições do triângulo equilátero:
reta 1: {:.0f}\n reta 2: {:.0f}\n reta 3: {:.0f} \n 
São iguais, assim pode formar-se um triãngulo equilatéro! \n'''.format(a, b, c))

else:
    print('''Dada as condições do triângulo equilátero:
 reta 1: {:.0f}\n reta 2: {:.0f}\n reta 3: {:.0f}
Não são iguais, assim não pode-se formar um triãngulo equilátero!\n'''.format(a, b, c))

if a == c and b == c and a != b:
    print('''Dada as condições do triângulo isósceles:
  reta 1: {:.0f}\n reta 2: {:.0f}\n reta 3: {:.0f}\n
Sendo que reta 1 e reta 2 são iguais e reta 1 # de reta 3, assim pode-se formar um triãngulo isósceless!'''.format(a, b, c))

else:
    print('''Dada as condições do triângulo isósceles:
  reta 1: {:.0f}\n reta 2: {:.0f}\n reta 3: {:.0f} \n
Não são iguais, assim não pode-se formar um triãngulo isósceles!'''.format(a, b, c))

