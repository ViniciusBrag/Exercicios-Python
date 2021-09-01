def notas(*num, sit=False):
    """

    :param num: números estabelecidos pelo usuário
    :param sit: situação opcional
    :return: retorna o dicionário com as informações da turma
    """
    ficha = dict()
    ficha['TOTAL'] = len(num)
    ficha['MAIOR'] = max(num)
    ficha['MENOR'] = min(num)
    ficha['média'] = sum(num) / len(num)
    if sit:
        if ficha['média'] > 7:
            ficha['Situação'] = 'Boa'
        elif ficha['média'] >= 5:
            ficha['Situação'] = 'Razoavél'
        else:
            ficha['Situação'] = 'Ruim'
    return ficha


#programa principal
resp = notas(2, 4, 6, 8.9, )
print(resp)