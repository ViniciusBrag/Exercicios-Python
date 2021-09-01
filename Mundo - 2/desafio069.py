contmulher20 = conthomen = contpessoas = 0
while True:
    print('==' * 20)
    print('CADASTRE UMA PESSOA')
    print('==' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        print('==' * 20)

    if idade > 18:
        contpessoas += 1
    if sexo == 'F' and idade < 20:
        contmulher20 += 1
    if sexo == 'M':
        conthomen += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 20)
print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18 anos: {contpessoas}')
print(f' Ao todo temos {conthomen} homens cadastrados')
print(f' E temos {contmulher20} mulheres cadastradas com menos de 20 anos')

