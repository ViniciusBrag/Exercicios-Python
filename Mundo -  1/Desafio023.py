print('=' * 4, 'Desafio ', '=' * 4)

n = int(input('Digite um número qualquer: '))
num = str(n)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))