print('=' * 4, 'Desafio ', '=' * 4)


a = float(input('Digite o primeiro número:'))
b = float(input('Digite o segundo número:'))
print('==' * 12)
maior = a
if (b>a):
    b = 'Segundo valor'
    print('O maior valor é o {}'.format(b))
elif (a>b):
    a = 'Primeiro valor'
    print('O maior valor é o {}'.format(a))
elif (a == b):
    a = 'Primeiro valor'
    b = 'Segundo valor'
    print('O {} e o {} são iguais portanto, não existe valore MAIOR.'.format(a, b))
print('==' * 12)