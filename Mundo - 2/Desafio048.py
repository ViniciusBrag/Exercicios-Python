print('=' * 4, 'Desafio ', '=' * 4)
cont = 0
s = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s += c
        cont += 1
print('A soma de todos os {} números impares são de {}' .format(cont, s))
print('FIM')
