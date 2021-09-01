print('=' * 4, 'Desafio 013', '=' * 4)
n = str(input('Olá digite seu nome: '))
sal = float(input('Qual é o seu salario? '))
au = sal*15/100
total = au+ sal
print('{} seu novo salário é de {:.1f}'.format(n, total))