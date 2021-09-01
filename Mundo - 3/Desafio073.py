bras = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras',
               'Santos', 'Athletico-PR', 'Bragantino', 'Ceará SC', 'Corinhians', 'Atlético-GO', 'Bahia', 'Sport Recife',
               'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')

print(bras)
print('Os Primeitos colocados são: {} {} {} '.format('\033[32m', bras[:4], '\033[m'))
print('Os Últimos colocados são: {} {} {} e Estão Rebaixados '.format('\033[31m', bras[-4:], '\033[m'))
print(f' Em Ordem {sorted(bras)}')
print(f' O Bahia está na {bras.index("Bahia") + 1} na posição')

