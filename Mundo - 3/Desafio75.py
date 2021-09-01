num = (int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o último número: ')))
print(f'Os números digitados foram: {num} ')
print(f' Apareceu {num.count(9)} vezes o número 9!')
if 3 in num:
    print(f' O Número 3 apareceu na {num.index(3) + 1} posição')
else:
    print('O número 3 não foi digitado ')
print('Os valores digitados Pares foram: ', end='')
for n in num:
    if n % 2 == 0:
      print(n, end=' ')

