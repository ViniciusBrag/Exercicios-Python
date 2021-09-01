def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor , digite um número inteiro: ')
            continue
        except (KeyboardInterrupt):
            print('\n Entrada de dados interrupido pelo usuário')
            return 0
        else:
            return n

def leiareal(msg):
    while True:
        try:
            bn = float(input(msg))
        except (ValueError, TypeError):
            print('Error: por favor, diite um número real: ')
        except (KeyboardInterrupt):
            print('\n '
                  'Entrada de dados interrupido pelo usuário')
            return 0

        else:
            return bn
