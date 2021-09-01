from math import hypot
print('=' * 4, 'Desafio 017', '=' * 4)
catetoa = float(input('Digite o cateto oposto: '))
catetob = float(input('Digite o cateto adjacente: '))
hp = hypot(catetoa, catetob)
print('A hipotenusa entre {} e {} = {:.2f}'.format(catetoa, catetob, hp))
