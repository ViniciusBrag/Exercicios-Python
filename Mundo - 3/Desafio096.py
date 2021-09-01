def área(largura, comprimento):
    a = largura * comprimento
    print(f'Á área de um terreno {largura} x {comprimento} é de {a}m')


print(' Controle de terrenos ')
print('--' * 20)
l = float(input('LARGURA (M):  '))
c = float(input('COMPRIMENTO (M): '))
área(l, c)
