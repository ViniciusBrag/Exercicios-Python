print('=' * 4, 'Desafio 011', '=' * 4)
print('1 litro de tinta pinta aproxidamente 2m2. 1l=2m2')
n = str(input('Qual o seu nome? '))
print('Bem vindo {:^10}'.format(n))
al = float(input('Qual é altura da parede que você deseja pintar: m² '))
lar = float(input('Qual a largura dessa parede que você deseja pintar: m²'))
am2 = lar * al
litros = am2/2
print('{} a área que você deseja pintar equivale {:.1f} m²! \n Você vai precisar de {:.2f}L de tinta aproxidamente'.format(n,am2, litros))


