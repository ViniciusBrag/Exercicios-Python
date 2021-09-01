def metade(num, sit=False):
    if sit:
        sit = 'R$'
        return (f'{sit}{num / 2:.2f}')
    else:
        return num / 2

def dobro(num, sit=False):
    if sit:
        sit = 'R$'
        return (f'{sit}{num / 2:.2f}')
    else:
        return num * 2


def aumentar(num, x=0, sit=False):
    if sit:
        sit = 'R$'
        return (f'{sit}{(num / 1000 * x * 10) + num:.2f}')
    else:
        return (num / 1000 * x * 10) + num


def dimninuir(num, x=0, sit=False):
    if sit:
        sit = 'R$'
        return (f'{sit}{num - (num / 1000 * x * 10):.2f}')
    else:
        return num - (num / 1000 * x * 10)

def moeda(num=0, moeda = 'R$'):
    return (f'{moeda}{num:.2f}'.replace('.', ','))