def leiadinheiro(msg):
    ok = False
    while not ok:
        p = str(input(msg)).replace(',', '.').strip()
        if p.isalpha() or p == '':
            print(f'\033[31mError "{p}" não é valido! \n Digite um número válido.\033[m')
        else:
            ok = True
            return float(p)