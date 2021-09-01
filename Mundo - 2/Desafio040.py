print('=' * 4, 'Desafio ', '=' * 4)

cores = {'vermelho': '\033[31m', 'limpa': '\033[m', 'amarelo': '\033[33m ', 'verde': '\033[32m'}
print('==' * 10)
print('{} MÉDIAS {}'.format(cores['amarelo'], cores['limpa']))
print('==' * 10)

nome = str(input('Digite seu nome: \n')).title()
n1 = float(input('Digite a sua primeira nota: \n '))
n2 = float(input('Digite a sua segunda nota: \n '))
MEDIA = (n1 + n2) / 2
if MEDIA <= 5:
    print('{}:\n MÉDIA {}, \n {} REPROVADO {}!!'.format(nome, MEDIA, cores['vermelho'], cores['limpa']))
elif (MEDIA > 5) and (MEDIA <= 6.9):
    print('{}:\n MÉDIA {}, \n {} RECUPERAÇÃO {}!!'.format(nome, MEDIA, cores['amarelo'], cores['limpa']))
else:
    print('{}:\n MÉDIA {}, \n {} APROVADO {}!!'.format(nome, MEDIA, cores['verde'], cores['limpa']))
print('==' * 10)
print('==' * 10)