print('GERADOR DE PA')
print('-=' * 15)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = a1
cont = 1
mais = 10
n = 0
while mais != 0:
    n = n + mais
    while cont <= n:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('Pausa')
    n = int(input('Quantos termos voce quer mostra a mais: '))
print('NENHUM TERMO...')
print('FIM')
