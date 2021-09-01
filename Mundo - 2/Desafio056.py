print('{} Olá Bem Vindo! {}'.format('\033[31m', '\033[m'))
media = 0
maior = 0
velho = ''
nova = 0
for n in range(1, 3):
    print('====== {} PESSOA ======'.format(n))
    nome = str(input(' Digite seu nome: \n ')).title()
    idade = int(input(' Digite sua idade {}{}{}: \n '.format('\033[32m', nome, '\033[m')))
    sexo = str(input(' SEXO: (M/F) \n ')).upper()
    if n == 1 and sexo == 'M':
        maior = idade
        velho = nome
    if idade > maior and sexo == 'M':
        maior = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        nova += 1
    media += idade / 4
print('A média de idade de grupo de pessoas é de {:.0f}'.format(media))
print('O Homem mais velho entre o grupo, foi {} com {} anos'.format(velho, idade))
if nova == 1:
    print(' Contém {} Mulher abaixo de 20 anos '.format(nova))
else:
    print(' Contém {} Mulheres abaixo de 20 anos '.format(nova))
