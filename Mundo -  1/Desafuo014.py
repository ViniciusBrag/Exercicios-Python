from math import floor
print('=' * 4, 'Desafio 013', '=' * 4)
c = float(input('Informe a temperatura em C: '))
f = 9 * c / 5 + 32
print('A temperatura {} C corresponde a {}F'.format(c, floor(f)))
