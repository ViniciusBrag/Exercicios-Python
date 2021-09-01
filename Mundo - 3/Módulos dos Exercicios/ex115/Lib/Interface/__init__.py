from time import sleep

from ex113.dados import *


def linha(tam=30):
    return '-' * 30


def cabeçalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        sleep(0.4)
        print(f'\033[33m{c}\033[33m - \033[34m{i}\033[34m ')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção:\033[m ')
    return opc

