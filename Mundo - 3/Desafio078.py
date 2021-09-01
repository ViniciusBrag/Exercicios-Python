valores = list()
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f' Você digitou: {valores}')
print(f'O maior valor digitado foi {maior} na Posições: {c} ', end='...') # valores{c} ele contem a quantidade que foi digitado
print(f'O Menor valor digitado foi {menor} na Posições: {c} ', end='...')

