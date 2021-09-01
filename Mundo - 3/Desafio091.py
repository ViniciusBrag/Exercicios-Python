from random import randint
from time import sleep
from operator import itemgetter

print('Valores sorteados')
dados = {}
ranking = list
for c in range(1, 5): # laço de repetição para repedir de jogador 1 a jogador 4
    num = randint(1, 7) # sorteador aleatoriamente um numero entre 1 e 7
    dados[f'Jogador{c}'] = num  # Jogador dentro de dicionários jogador c == range de 1 a 4 recebe num == sorteados de 1 a 7
for i, v in enumerate(dados.items()):  # i == índice e v == valores de todos os items dentro do dicionário
    sleep(1)
    print(f'{i+1} Jogador Tirou: {v[1]}') # imprime i+1 para não começar do 0, v[1] apenas os valores e não o nome no caso 'Jogador'
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True) # itemgetter ordenar do maior valor para o menor.
for i, v in enumerate(ranking):  # i == índice e v == valores de todos os items dentro da lista
    print(f'{i+1} Lugar: {v[0]} com {v[1]}. ')  # v[0] nome do jogador e v[1] quantidade de pontos
    sleep(0.8)