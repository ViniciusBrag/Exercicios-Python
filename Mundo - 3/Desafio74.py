from random import randint

num = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print('Os números sorteados: ')
for n in num:
    print(f'{n}', end='  ')

print(f'''
Maior valor sorteado: {max(num)  }
Menor valor sorteado: {min(num)}.''')
