print('GERADOR DE PA')
print('-=' * 15)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = a1
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')


