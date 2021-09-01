listagem = ('Lápis', 1.75, 'Borracha', 2.00,
            'Caderno', 15.90, 'Estojo', 25.00, 'Mochila',
            120.90,
            'Livro', 100.90)
print('===' * 12)
print(f'{"LISTAGEM DE PREÇOS":^30}  ') #alinhar no meio a string

print('===' * 12)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='') #alinhou a esquerda (:.<30)
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
