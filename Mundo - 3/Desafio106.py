from time import sleep
c = ('\033[30m',  # 0 sem cor
     '\033[0;30;41m',  # 1 vermelho
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30'
     );


def ajuda(com):
    titulo(f'ACESSANDO MANUAL DO COMANDO \'{com}\'', 4)
    print(c[6], end=' ')
    help(com)
    print(c[0], end=' ')
    sleep(0.2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    if tam:
        print(c[cor], end=' ')
        print('~' * tam)
        print(f'  {msg}')
        print('~' * tam)
        print(c[0], end=' ')
        sleep(0.3)




comando = ''
while True:
    titulo('SISTEMA AJUDA HELP', 2)
    comando = str(input("Função ou Biblioteca? "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)