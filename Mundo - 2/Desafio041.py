print('=' * 4, 'Desafio ', '=' * 4)

from datetime import date

cores = {'vermelho': '\033[31m',  'limpa': '\033[m', 'amarelo': '\033[33m ', 'verde': '\033[32m',  'azul': '\033[34m'''}
print('==' * 10)
print('{} NATAÇÃO {}'.format(cores['azul'], cores['limpa']))
print('==' * 10)
nome = str(input('Digite seu nome: ')).title()
nasc = int(input('Digite apenas o ano do seu nascimento: Ex:(**/**/1965: \n '))
ano = (date.today().year - nasc)
if ano <= 9:
    print('Idade: {} \n {} -  CATEGORIA: MIRIN '.format(ano, nome))
elif (ano > 9) and (ano <= 14):
    print('Idade: {} \n {} -  CATEGORIA: INFANTIL'.format(ano, nome))
elif (ano > 14) and (ano <= 19):
    print('Idade: {} \n {} -  CATEGORIA: JUNIOR'.format(ano, nome))
elif (ano > 19) and (ano <= 20):
    print('Idade: {} \n {} -  CATEGORIA: SÊNIOR'.format(ano, nome))
else:
    print('Idade: {} \n {} -  CATEGORIA: MASTER'.format(ano, nome))
print('==' * 10)
print('==' * 10)