list = []
par = []
impar = []
while True:
    print('-=' * 30)
    n = int(input('Digite um valor para VERIFICAÇÃO: '))
    r = str(input('Quer continuar? [S/N] '))
    if n not in list:
        list.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if r in 'nN':
        break
print('-=' * 30)
print(f'A lista completa:', end='')
print(list)
print(f'A lista de pares:', end='')
print(par)
print(f'A Lista de ímpares:', end='')
print(impar)
