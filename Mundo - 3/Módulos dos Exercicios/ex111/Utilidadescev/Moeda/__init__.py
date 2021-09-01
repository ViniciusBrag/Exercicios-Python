def metade(num=0, sit=False):
    """
    Retornando o valor com ou sem formatação
    :param num: valor a ser analisado
    :param sit: se deseja ser formatado ou não
    :return: valor verificado
    """
    res = num / 2
    return res if sit is False else moeda(res)


def dobro(num=0, sit=False):
    res = num * 2
    return res if sit is False else moeda(res)


def aumentar(num=0, x=0, sit=False):
    res = (num / 1000 * x * 10) + num
    return res if sit is False else moeda(res)


def dimninuir(num=0, x=0, sit=False):
    res = num - (num / 1000 * x * 10)
    return res if sit is False else moeda(res)

def moeda(num=0, moeda = 'R$'):
    return (f'{moeda}{num:.2f}'.replace('.', ','))


def resumo(num=0, incre=10, decre=10):
    print('--' * 15)
    print('RESUMO DO VALOR'.center(15))
    print('--' * 15)
    print(f'Preço analisado:    \t{moeda(num)}')
    print(f'Dobro do preço:     \t{dobro(num,True)}')
    print(f'Metade do preço:    \t{metade(num, True)}')
    print(f'{incre}% de aumento: \t\t{aumentar(num, incre, True)}')
    print(f'{decre}% de redução: \t\t{dimninuir(num, decre, True)}')
    print('--' * 15)