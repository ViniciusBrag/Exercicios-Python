print('=' * 4, 'Desafio ', '=' * 4)

print('Olá bem vindo! ')
nome = str(input('Qual o seu nome: \n ')).capitalize().strip()
vel = float(input('Qual era a velocidade que você estava percorrendo a via? Km/h \n '))
if vel > 80:
    print('Você ultrapassou {:.0f}Km acima do permitido \n A multa é de {:.1f}$'.format(vel - 80, (vel - 80) * 7.0))
else:
    print('{} você passou dentro limite, dirigi com cuidado! \n'.format(nome))
print('==FIM==')
