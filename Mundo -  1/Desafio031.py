print('=' * 4, 'Desafio ', '=' * 4)

nome = str(input('Digite seu nome: \n ')).title().strip()
viagem = float(input('Digite a distância a ser percorrida: Km \n '))
if viagem <= 200:
    print('{}, o valor da sua passagem é de {:.2f}$'.format(nome, (viagem * 0.50)))
else:
    print('{}, o valor da sua passagem é de {:.2f}$'.format(nome, (viagem * 0.45)))
    print('==FIM==')