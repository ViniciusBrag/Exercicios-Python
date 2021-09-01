print('=' * 4, 'Desafio ', '=' * 4)

nome = str(input('Digite o nome completo:')).strip()
print('o nome completo digitado foi {}'.format(nome.title()))
divisao = nome.split()
print('Primeiro:{}'.format(divisao[0].capitalize()))
print('O Último: {}'.format(divisao[len(divisao) - 1].capitalize()))

