print('=' * 4, 'Desafio 007', '=' * 4)
n = input('Qual o seu nome ? ')
nota1 = float(input('Digite sua Primeira nota: '))
nota2 = float(input('Digite sua Segunda nota: '))
nota3 = float(input('Digite sua Terceira nota: '))
nota4 = float(input('Digite sua Quarta nota:  '))
m = (nota1 + nota2 + nota3 + nota4)/4
print('{} Sua média foi de {:.3f}'.format(n, m))

