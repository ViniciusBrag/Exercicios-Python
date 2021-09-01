def fatorial(num=1, show=False):
    """
    Calculo de FATORIAL
    :param num: Valor para calcular fatorial. 
    :param show: (opcional) Mostrar ou não a conta.
    :return: retorna resultado como o usuário deseja.
    """""
    fat = 1
    for c in range(num, 0, -1):
        if show:
          print(c, end=' ')
          if c > 1:
            print('X', end=' ')
          else:
            print(' = ', end=' ')
        fat *= c
    return fat


print(fatorial(5, show=True))
help(fatorial)