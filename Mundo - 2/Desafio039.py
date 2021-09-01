print('=' * 4, 'Desafio ', '=' * 4)

print('==' * 20)
from datetime import date

nome = str(input('Digite seu nome: \n ')).title()
nasc = int(input('Digite apenas o ano do seu nascimento: Ex:(**/**/1965: \n '))
ano = (date.today().year - nasc)
if ano < 18:
    print(''' Olá {} sua idade é de {} anos, não precisa se alistar ao Serviço Militar 
ainda falta {} anos.'''.format(nome, ano, 18 - ano))
elif ano == 18:
    print('Olá {} sua idade é de {} anos, você precisa se alistar ao Serviço Militar!!'.format(nome, ano))
else:
    print(''' Olá {} sua idade é de {} anos, você não precisa se alistar ao Serviço Militar já se passaram {} anos 
'''.format(nome, ano, ano - 18))
print('==' * 20)
