from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 a 10')
print('Será que você consegue advinhar?')
nome = str(input('Qual o seu nome?\n')).capitalize()
vezes = 0
num = int(input('Informe seu número entre 0 a 10: \n '))
sor = randint(0, 10)

while num != sor:
    if num <= 10:
        num = int(input('Informe outro número 0 a 10: \n '))
        vezes += 1
    if num >= 10:
        print('{}OPERAÇÃO INVÁLIDA{}'.format('\033[31m', '\033[m'))
        num = int(input('Informe outro número 0 a 10: \n '))
    if sor > num:
        print('Mais..tente mais uma vez... ')
    if sor < num:
        print('Menos... tente mais uma vez...')

print('Parabéns você acertou {}'.format(nome))
print('{} precisou de {} vezes para ganhar'.format(nome, vezes))
