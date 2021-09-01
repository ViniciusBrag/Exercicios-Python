from random import randint
contganho = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR ')
print('-=' * 20)
while True:
    n = int(input('Digite um valor: '))
    parouimpar = ' '
    while parouimpar not in 'PI':
        parouimpar = str(input('PAR OU IMPAR? (P/I): ')).upper().strip()[0]
        pc = randint(0, 10)

    if parouimpar == 'P':
        soma = n + pc
        if soma % 2 == 0:
            print(f'Você jogou {n} e o computador {pc}. Total deu = {soma} PAR')
            print('VOCẼ VENCEU')
            print('-=' * 20)
            contganho += 1
        if soma % 2 == 1:
            print(f'Você jogou {n} e o computador {pc}. Total deu = {soma} ÍMPAR')

    elif parouimpar == 'I':
        soma = n + pc
        if soma % 2 == 1:
            print(f'Você jogou {n} e o computador {pc}. Total deu = {soma} IMPAR')
            print('VOCẼ VENCEU')
            print('-=' * 20)
            contganho += 1
        if soma % 2 == 0:
            print('VOCÊ PERDEU!')
            print('-=' * 20)
            break
    else:
        print('OPERAÇÃO INVÁLIDA...')
    print('Vamos jogar novamente..')
print(f'GAME OVER! Você venceu {contganho} vezes')
