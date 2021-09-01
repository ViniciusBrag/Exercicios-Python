print('=' * 4, 'Desafio ', '=' * 4)

print('Olá Bem vindo')
nome = str(input('Digite seu nome: ')).title()
valor = float(input('Digite o preço do produto:R$ '))
print('Opção:\n{} ( 1 ) Á Vista \n ( 2 ) Cartão Á Vista \n ( 3 ) 2x no Cartão \n (4) 3x ou mais{}'.format('\033[34m)', '\033[m'))
cond = int(input('Digite a opção de pagamento: '))
if cond == 1:
    print('Olá {}, Compra aprovada. \n {}$ À vista'.format(nome, valor - (valor * 10 / 100)))
elif cond == 2:
    print('Olá {}, Compra aprovada. \n {}$  Cartão Á vista'.format(nome, valor - (valor * 5 / 100)))
elif cond == 3:
    print('Olá {}, Compra aprovada.\n {}$ Crédito (2x)'.format(nome, valor))
if cond == 4:
    op = int(input('Digite a quantidade de parcelas: '))
    print('Olá {}, Obrigado por efetuar a compra. \n {}$ Crédito {}x '.format(nome, valor + (valor * 20/100), op))
else:
    print(''' {}  OPERAÇÃO INVÁLIDA DE PAGAMENTO, TENVE NOVAMENTE {} 
    '''.format('\033[31m] ', '\033[31m]'))