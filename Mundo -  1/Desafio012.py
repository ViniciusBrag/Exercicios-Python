print('=' * 4, 'Desafio 012', '=' * 4)
print('Loja toda com 5% de desconto aproveite!')
n = str(input('Qual o seu nome? '))
v = float(input('Digite o valor do produto desejado $:'))
des = (v*5/100)
total = v - des

print('Obrigado pela sua compra senhor {}, o seu produto com desconto é de {:.2f}$ reais'.format(n, total))
