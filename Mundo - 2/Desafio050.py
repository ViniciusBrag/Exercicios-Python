soma = 0
negados = 0
sn = 0
for c in range(0, 7):
    num = int(input('Digit um número: '))
    if num % 2 == 0:
        soma += + num
    elif num % 2 == 1:
        negados += 1
        sn += + num
    else:
        print('INVÁLIDO')
print('---------------')
print('A soma dos números pares digitados foi de {}'.format(soma))
print('Foram {} números negados e a soma de números impares são de {} '.format(negados, sn))
