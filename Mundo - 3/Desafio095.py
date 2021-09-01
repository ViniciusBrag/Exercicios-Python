dados = {}
cadagol = []
listatudo = []
totalgols = 0

while True:
    dados.clear()
    nome = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas o {nome} jogou? '))

    cadagol.clear()
    for c in range(0, partidas + 1):
        gols = int(input(f'   Quantos Gol na partida {c}: '))
        cadagol.append(gols)

    dados['Nome'] = nome
    dados['Gols'] = cadagol[:]
    dados['Total'] = sum(cadagol)
    listatudo.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
             break
        print('Error')
    if resp == 'N':
      break

print('-=' * 30)
print(f'cod  ', end='')
for i in dados.keys():
    print(f'{i:<15}', end=' ')
print()
print('-=' * 30)
for k, v in enumerate(listatudo):
    print(f'{k:>4}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-=' * 30)
print('-' * 45)
while True:
    opc = int(input('Mostrar dados de qual jogador? '))
    if opc == 999:
        print('Finalizando...')  # Finalizar programa
        break
    if opc >= len(listatudo):
        print(f'Error! não existe jogador com comando {opc}. Tente novamente')
        print('-=' * 30)
    else:
        if opc <= len(listatudo) - 1:
            print(f'-- Levantamento do jogador {listatudo[opc]["Nome"]} ')
        for i, v in enumerate(dados['Gols']):
            print(f'No jogo {i} fez {v} Gols')



#print(f'O Jogador {dados["Nome"]} jogou {partidas} partidas.')
#for i, v in enumerate(dados['Gols']):
    #print(f'         => Na partida {i}, fez {v} gols')
#print(f'Foi um total de {dados["Total"]} Gols ')