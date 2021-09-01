cont = 0
n = 0
total = 0
n = int(input('Digite números inteiros: '))
while n != 999:
    total += n
    cont += 1
    n = int(input('Digite números inteiros: '))
print(total)
print(cont)
print('terminou')
