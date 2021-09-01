print('=' * 4, 'Desafio ', '=' * 4)

from random import randint


print('Bem vindo ao jogo contra a MACHINE!')
print('Nesse jogo o computador vai escolher um número de 0 a 5, você precisa acertar o mesmo número GOOD LUCK!!')
nome = str(input('Qual o seu nome?\n')).capitalize().strip()
num = int(input('Informe seu número entre 0 a 5: \n '))
sor = randint(0, 5)
print('Número escolhido foi {}'.format(sor))

if num == sor:

    print(' {} PARABÉNS {} você acertou {} !!! '.format('\033[32m', nome, '\033[m'))
else:
    print(' \033[31m Que pena :/, tente outra vez \033[m ')
print('Fim de jogo!')
