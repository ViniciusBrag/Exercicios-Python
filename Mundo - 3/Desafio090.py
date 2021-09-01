dados = {}
boletim = []
situação = str

while True:
    nome = str(input('Nome: '))
    media = float(input(f'Média de {nome}: '))
    if media >= 7:
        situação = 'APROVADO'
    elif 5 <= media < 7:
        situação = 'RECUPERAÇÃO'
    else:
        situação = 'REPROVADO'
    dados['Nome'] = nome
    dados['Média'] = media
    dados['Situação'] = situação
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'N':
         break

boletim.append(dados.copy())
for d in boletim:
    for k, v in d.items():
        print(f'O {k} é igual {v}')
