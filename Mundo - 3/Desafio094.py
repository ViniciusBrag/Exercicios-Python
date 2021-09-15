dados = {'Nome': [], 'Sexo': [], 'Idade': [], 'Totmulheres': [], 'Acimamedia': []}
media = 0
while True:
    nome = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'fF' or sexo in 'mM':
            break
        print('Error')
    idade = int(input('Idade: '))


    dados['Nome'].append(nome)
    dados['Sexo'].append(sexo)
    dados['Idade'].append(idade)

    if idade > 0:
        media += idade
    if sexo == 'F':
        dados['Totmulheres'].append(nome)

    if idade > (media / len(dados['Nome'])):
        dados['Acimamedia'].append(nome)
        dados['Acimamedia'].append(sexo)
        dados['Acimamedia'].append(idade)

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
             break
        print('Error')
    if resp == 'N':
        break

print(f'Foram cadastrada {len(dados["Nome"])} pessoas')
print(f'A média do grupo é de {media / len(dados["Nome"]):.0f} anos')
print(f'As Mulheres cadastradas são {len(dados["Totmulheres"])}: ')
for p in dados['Totmulheres']:
    print(p)
print()

print(f'lista das pessoas acima da média')
for dado in dados["Acimamedia"]:
    if dado == nome:
        print(dado)




