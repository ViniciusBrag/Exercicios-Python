num = int(input('Digite um número? '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += + 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c))
print('\033[mO nùmero {} foi divisivel {} vezes '.format(num, tot))
if tot == 2:
    print('Devido a isso ele é PRIMO')
else:
    print('Devido a ser divisivel {} ele não é primo'.format(tot))