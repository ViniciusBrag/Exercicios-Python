print('=' * 4, 'Desafio ', '=' * 4)

cores = {'vermelho': '\033[32m', 'limpa': '\033[m'}

print('{}***{}'.format(cores['vermelho'], cores['limpa']) * 10)
print('Calculando IMC')
print('{}***{}'.format(cores['vermelho'], cores['limpa']) * 10)

nome = str(input('Digite seu nome: ')).title()
peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = (peso) / (altura * altura)

if IMC <= 18.5:
    print('{}, seu IMC: {:.2f} está abaixo do peso!'.format(nome, IMC))
elif IMC > 18.5 or IMC >= 25:
    print('{}, seu IMC: {:.2f} você está no seu peso ideal, parabéns continua assim'.format(nome, IMC))
elif IMC >= 25 or IMC <= 30:
    print('{}, seu IMC: {:.2f} SOBREPRESO, cuidado cuida-se'.format(nome, IMC))
elif IMC > 30 or IMC > 40:
    print('{}, seu IMC: {:.2f} OBESIDADE, procura seu médico urgente'.format(nome, IMC))
else:
    print('{}***{}'.format(cores['vermelho'], cores['limpa']) * 10)
    print('FIM')
    print('{}***{}'.format(cores['vermelho'], cores['limpa']) * 10)
