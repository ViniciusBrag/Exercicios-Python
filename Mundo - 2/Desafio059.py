nome = str(input('Digite seu nome: ')).upper()
n = int(input('Digite um valor: '))
n1 = int(input('Digite outro valor: '))
op = 0
while op != 6:
    print('''     MENU 
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR
''')
    op = int(input('Digite a sua escolha: '))
    print('--=' * 20)
    if op == 1:
        somar = + n + n1
        print('OPÇÃO {}'.format(op))
        print(' número digitados: {} + {} == {}'.format(n, n1, somar))
        print('--=' * 20)
    elif op == 2:
        multiplicar = n * n1
        print('OPÇÃO {}'.format(op))
        print(' número digitados: {} * {} == {}'.format(n, n1, multiplicar))
        print('--=' * 20)
    elif op == 3:
        if n > n1:
            maior = n
        else:
            maior = n1
        print('OPÇÃO {}'.format(op))
        print(' número digitados: {} e {} MAIOR == {}'.format(n, n1, maior))
        print('--=' * 20)
    elif op == 4:
        print('OPÇÃO {}'.format(op))
        print('Adcionar novos números')
        n2 = int(input('Digite um novo número: '))
        n3 = int(input('Digite outro novo número: '))
        print('Cadastrado com sucesso, {} e {}'.format(n2, n3))
        print('--=' * 20)
    else:
        print('OPERAÇÃO INVÁLIDA')
        print('--=' * 20)

print('SAINDO DO PROGRAMA....')
print('Obrigado {}'.format(nome))
