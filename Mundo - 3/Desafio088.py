from random import randint
print('==' * 20)
str = 'JOGO NA MEGASENA'
print(f'{str:^20}')    # apresentação do jogo
print('==' * 20)

lista = [] # lista fora para ela adcionar e não renderizar um novo e substituir
cont = 0  # cont para o randint
quant = int(input('Quantos jogos você quer que eu sorteio: ')) # quantidade que o usuário quer jogar.
tot = 1
jogos = [] # outra lista para adcionar a lista dos números sorteados
while tot <= quant:
    cont = 0  # p   ara randomizar os 6 números e colocar em cada parte da lista
    while True:
        num = randint(0, 60)
        if num not in lista: # Se não estiver dentro da lista adcione
            lista.append(num)  # adcionando
            cont += 1   # para cada número sorterado ele conta 1 vez.
        if cont == 60: # Atingindo 6 números sorteados pare.
            break
    lista.sort()  # os números sorteados ser de forma ordenados
    jogos.append(lista[:]) # copia da lista para jogos.
    lista.clear() # apagar a lista.
    tot += 1 # para não entrar em loop infinito
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos): # para indice do jogo mostra a lista sorteada
    print(f'Jogo {i + 1}:{l}')
    print()
print('-=' * 3, '< BOA SORTE! > ', '-=' * 3)

