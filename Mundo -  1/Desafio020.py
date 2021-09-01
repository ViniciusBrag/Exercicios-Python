from random import shuffle

print('=' * 4, 'Desafio 020', '=' * 4)
a = str(input('Digite o nome do aluno: '))
b = str(input('Digite o nome do aluno: '))
c = str(input('Digite o nome do aluno: '))
d = str(input('Digite o nome do aluno: '))
list = [a, b, c, d]
shuffle(list)
print('A ordem vai ser: ')
print(list)
