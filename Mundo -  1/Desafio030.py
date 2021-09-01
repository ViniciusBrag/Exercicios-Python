print('=' * 4, 'Desafio ', '=' * 4)

num = float(input('Digite um número: '))
if num % 2 == 0:
    print('O número {:.0f} é PAR'.format(num))
else:
    print('O numero {:.0f} é IMPAR \n'.format(num))
    print('==FIM==')