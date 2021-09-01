print('=' * 4, 'Desafio ', '=' * 4)

print('Olá bem vindo!')
nome = str(input('Digite seu nome: \n ')).title().title()
sal = float(input('Digite o seu sálario atual:$ '))
if sal > 1250:
    nvsal = (sal * 10)/100 + sal
    print('{} o seu novo sálario com aumento de 10% é de {:.2f}$'.format(nome, nvsal))
if sal <= 1250:
    nvsal1 = (sal * 15)/100 + sal
    print('{} o seu novo sálario com aumento de 15% é de {:.2f}$'.format(nome, nvsal1))