cont = media = total = maior = menor = 0
resp = 'S'
while resp != 'N':
    n = int(input('Digite um número inteiro: '))
    resp = str(input('Quer continuar? Digite: (S/N)')).upper().strip()[0]
    if n > 0:
        cont += 1
        total += n
        media = total / cont
    if n > maior:
        maior = n
    if n < maior:
        menor = n
print('Foram {} números digitados é o maior entre eles é {}'.format(cont, maior))
print('Foram {} números digitados é o menor entre eles é {}'.format(cont, menor))
print('A média dos {} números digitados foi de {:.2f}'.format(cont, media))
print('Fim')
