from ex107 import Moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {Moeda.metade(p)}')
print(f'O dobro de {p} é {Moeda.dobro(p)}')
print(f'Aumentando 10% de {p} temos {Moeda.aumentar(p, 20)}')
print(f'Diminuindo 13% de {p} temos {Moeda.dimninuir(p, 13)}')