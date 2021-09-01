dados = list()
pessoas = []
leves = pesados =  0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso:  ')))
    pessoas.append(dados[:])
    dados.clear()
    for dp in pessoas:
        if dp == 0:
            leves = dp[1]
            pesados = dp[1]
        else:
            if dp[1] > pesados:
                pesados = dp[1]

            if leves < dp[1]:
                dp[1] = leves

    resp = input('Quer continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break
print(f'Os dados foram {pessoas}')
print(f' Voce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {pesados}Kg ')
print(f'O menor peso foi de {leves}Kg ')