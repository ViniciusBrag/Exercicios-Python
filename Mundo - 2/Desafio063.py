print('SEQUÊNCIA DE FIBONACCI')
print('-=' * 15)
total = int(input('Digite  o total de elementos da sequencia: '))
cont = 0
t1 = 0
t2 = 1
while cont != total:
    cont += 1
    t3 = t2 + t1
    t1 = t2
    t2 = t3
    print('{} -> '.format(t3), end='')
print('FIM')