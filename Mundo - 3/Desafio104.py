# programa principal
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mError! Digite um número inteiro\033[m')
        if ok: # if ok for == True para e retorna o valor como (int)
            break
    return valor

n = leiaint('Digite um número: ')
print(f'Você digitou número {n}')
