from random import choices
print('=' * 4, 'Desafio 017', '=' * 4)
a = str(input('Digite o nome do aluno: '))
b = str(input('Digite o nome do aluno: '))
c = str(input('Digite o nome do aluno: '))
d = str(input('Digite o nome do aluno: '))
sor = (a, b, c, d)
escolhido = choices(sor)
print('O aluno escolhido foi {}'.format(escolhido))



