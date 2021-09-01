num = int(input('Digite um número: '))
contador = num
f = 1
print('Calculando {}! = '.format(num), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' X ' if contador > 1 else ' = ', end='')
    f *= contador
    contador -= 1
print('{}'.format(f))

