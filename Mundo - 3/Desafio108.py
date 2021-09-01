from ex108 import Moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.metade(p))}')
print(f'O dobro de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.dobro(p))}')
print(f'Aumentando 10% de {p} temos {Moeda.moeda(Moeda.aumentar(p, 20))}')
print(f'Diminuindo 13% de {p} temos {Moeda.moeda(Moeda.dimninuir(p, 13))}')