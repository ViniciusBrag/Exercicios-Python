print('=' * 4, 'Desafio ', '=' * 4)

nome = str(input('Digite uma frase qualquer:')).upper()
print('a letra A se repete \n {} vezes.'.format(nome.count('A')))
print('A letra A aparece primeira vez na posição {}'.format(nome.find('A') + 1))
print('A letra A aparece ultima vez na posição {}'.format(nome.rfind('A') + 1))
