from ex109 import Moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {Moeda.moeda(p)} é {Moeda.metade(p, False)}')
print(f'O dobro de {Moeda.moeda(p)} é {Moeda.dobro(p, False)}')
print(f'Aumentando 10% de {Moeda.moeda(p)} temos {Moeda.aumentar(p, 10, False)}')
print(f'Diminuindo 13% de {Moeda.moeda(p)} temos {Moeda.dimninuir(p, 13, False)}')