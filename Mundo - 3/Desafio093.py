dados = {}
cadagol = []
totalgols = 0

nome = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas o {nome} jogou? ')
               )
for c in range(0, partidas + 1):
    gols = int(input(f'Quantos Gol na partida {c}: '))
    cadagol.append(gols)
    totalgols += gols

dados['Nome'] = nome
dados['Gols'] = cadagol
dados['Total'] = totalgols

print('-=' * 30)
for i, v in dados.items():
    print(f'O campo {i} tem o valor {v}')
print('-=' * 30)

print(f'O Jogador {dados["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(dados['Gols']):
    print(f'         => Na partida {i}, fez {v} gols')
print(f'Foi um total de {dados["Total"]} Gols ')