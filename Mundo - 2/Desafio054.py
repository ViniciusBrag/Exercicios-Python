from datetime import date
maiores = 0
menores = 0
for n in range(1, 7):
    nome = str(input('Digite seu nome: ')).capitalize()
    nasc = int(input('Digite apenas o ano do seu nascimento, Ex: XX/XX/1996 : '))
    ano = date.today().year - nasc
    if ano >= 18:
        maiores += 1
    elif ano < 18:
        menores += 1
    if nasc > date.today().year:
        print('{}OPERAÇÃO INVÁLIDA{}'.format('\033[31m', '\033[m'))
if maiores > 1:
    print('{} pessoas atingiram a maioridade '.format(maiores))
else:
    print('{} pessoa atingiu a maioridade'.format(maiores))
if menores > 1:
    print('{} pessoas ainda não atingiram a maioridade'.format(maiores))
else:
    print('{} pessoa ainda não atingiu a maioridade '.format(maiores))
