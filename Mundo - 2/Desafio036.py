print('=' * 4, 'Desafio ', '=' * 4)

print('===' *12)
print('Empréstimo Bancário Consulte ')
print('===' * 12)

nome = str(input('Qual o seu nome: \n')).title()
print('Bem vindo {} \n'.format(nome))
Vcasa = float(input('Digite o valor da casa desejada:R$ \n'))
Sal = float(input(' Digite o valor do seu sálario atual:R$ \n '))
anos = int(input(' Digite a quantidade de anos que você deseja pagar: '))

meses = anos * 12
exceder = (Sal/100) * 30


print('{} o valor da prestação será de R${:.2f}'.format(nome, (Vcasa/meses)))
if (Vcasa/meses) > exceder:
    print('''{}, Desculpe seu empréstimo foi negado :/,Devido a prestação do empréstimo não pode ultrapassar os 30% do salário 
  do contratante. '''.format(nome))
else :
    print('{}, seu empréstimo foi aprovado , obrigado por escolher nossa empresa! '.format(nome))
print('==' * 12)

