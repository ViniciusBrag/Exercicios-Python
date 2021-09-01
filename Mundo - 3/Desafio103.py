def ficha(jog='<Desconhecido>', g=0):
    print(f'O jogador {jog} fez {g} gol(s) no campeonato')



# Programa principal

nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
