num = list()
while True:
    n = int(input('Digite um valor:  '))
    if n not in num:
        num.append(n)
        print('Valor adcionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adcionar...')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
         break
num.sort()
print(f'Os valores digitados: {num} ')
