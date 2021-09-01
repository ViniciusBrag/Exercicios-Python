print('=' * 4, 'Desafio 010', '=' * 4)
n = str(input('Qual seu nome? '))
reais = float(input('Quantos reais você tem na carteira $? '))
dolar = reais/3.27
print('Você tem {:.2f}$ para gastar! Muito Obrigado {}'.format(dolar, n))
