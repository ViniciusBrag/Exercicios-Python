from datetime import date
dados = {}

nome = str(input('Nome: '))
anonasc = int(input('Ano de nascimento: '))
ctps = int(input('Carteira De Trabalho (0 não tem): '))
dados['Nome'] = nome
dados['Data de Nascimento'] = anonasc
dados['CTPS'] = ctps
if ctps == 0:
    print('-=' * 30)
    for n, v in dados.items():
            print(f'O {n} tem valor {v}')
else:
    anodecontrat = int(input('Ano de contratação: '))
    sal = float(input('Salário: '))
    aposentadoria = (date.today().year - anodecontrat)
    dados['Contratação'] = anodecontrat
    dados['Salário'] = sal
    dados['Aposentadoria'] = aposentadoria
    for i, v in dados.items():
        print(f'O {i} tem valor {v}')


