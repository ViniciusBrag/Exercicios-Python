list = []
cont = 0
sim = str
while True:
    n = int(input('Digite um valor: '))
    if n not in (list):
        list.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Você digitou {len(list)} elementos: ', end='')
print(list)
list.sort(reverse=True)
if 5 in list:
    print('O valor 5 faz parte da lista')
    pos = [list.index(5) + 1]
    print(f'o 5 está na posição {pos}')
else:
    print('O valor 5 não faz parte da lista')

print(f'Os valores em ordem derescente são {list}')
