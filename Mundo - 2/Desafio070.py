totgasto = maiormil = barato = cont = 0
nomebarato = str
print('==' * 20)
print('LOJA BARATÃO')
print('==' * 20)
while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço R$: '))
    totgasto += preco
    cont += 1
    if cont == 1:
        barato = preco
        nomebarato = produto
    else:
        if preco < barato:
            barato = preco
            nomebarato = produto

    if preco > 1000:
         maiormil += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]:  ')).strip().upper()[0]
    if resp == 'N':
          break

print(f'Contém {maiormil} produtos maiores que R$1000')
print(f'Total gasto na sua compra foi de R${totgasto}')
print(f"O produto mais barato: {nomebarato}\n PreçoR$: {barato}")

