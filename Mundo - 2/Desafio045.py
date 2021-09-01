from random import randint
from time import sleep
print('=' * 4, 'Desafio ', '=' * 4)
print('-=' * 15)
print('JOKENPOOH')
print('-=' * 15)
cores = {'Amarelo': '\033[33m', 'Preto': '\033[30m', 'Vermelho': '\033[31m', 'fecha': '\033[m', 'azul': '\033[34m'}
lista = ['PEDRA', 'PAPEL', 'TESOURA']

computador = randint(0, 2)

print('''{} (0)PEDRA{}\n {}(1)PAPEL\n{} {}(2)TESOURA{}'''
      .format(cores['Preto'], cores['fecha'], cores['Amarelo'], cores['fecha'],  cores['Vermelho'], cores['fecha']))
jogador = int(input('Digite a sua escolha JOGADOR: '))
print('{} GO, GO, GO....'.format(cores['azul']))
sleep(1)
print('{}JO'.format(cores['Vermelho']))
sleep(0.5)
print('{}GAN'.format(cores['Vermelho']))
sleep(0.5)
print('{}DOOOO{}'.format(cores['Vermelho'], cores['fecha']))
print('-=' * 15)
print('COMPUTADOR = {}'.format(lista[computador]))
print('JOGADOR = {}'.format(lista[jogador]))
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print(' JOGADOR {}VENCEU{}'.format(cores['azul'], cores['fecha']))
    elif jogador == 2:
        print('JOGADOR {}PERDEU{}'.format(cores['Vermelho'], cores['fecha']))
    else:
        print('OPERAÇÃO INVÁLIDA {}:/{}'.format(cores['Vermelho'], cores['fecha']))

elif computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print(' JOGADOR {}VENCEU{}'.format(cores['azul'], cores['fecha']))
    elif jogador == 0:
        print('JOGADOR {}PERDEU{}'.format(cores['Vermelho'], cores['fecha']))
    else:
        print('OPERAÇÃO INVÁLIDA {}:/{}'.format(cores['Vermelho'], cores['fecha']))
elif computador == 2:
    if jogador == 2:
        print('EMPATE')
    elif jogador == 1:
        print(' JOGADOR {}VENCEU{}'.format(cores['azul'], cores['fecha']))
    elif jogador == 0:
        print('JOGADOR {}PERDEU{}'.format(cores['Vermelho'], cores['fecha']))
    else:
        print('OPERAÇÃO INVÁLIDA {}:/{}'.format(cores['Vermelho'], cores['fecha']))
else:
    print('OPERAÇÃO INVÁLIDA {}:/{}'.format(cores['Vermelho'], cores['fecha']))
