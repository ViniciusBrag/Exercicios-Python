cont = ('zero', 'Um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
        , 'Onze', 'Doze' 'Treze', 'Quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int
while True:
    n = int(input('Digite um número entre (0 e 20): '))
    if 0 <= n <= 20:
        break
print(f' Voce digitou o número {cont[n]}')
print('FIm')
