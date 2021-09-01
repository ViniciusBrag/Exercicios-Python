ficha = []
status = str
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    if media >= 7:
        status = 'APROVADO'
    else:
        status = 'REPROVADO'

    ficha.append([nome, [nota1, nota2], media, status])  # criar dentro da lista outra lista com índice
    #[0] = nome| [1] = nota1, nota2| [2] = media

    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'nN':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}{"STATUS":>16}')
print('-' * 45)
for i, a in enumerate(ficha): # I = Indice para cada nome, nota1, nota2 e média feita esse indice contar.
    #a vai correr dentro da lista.
    print(F'{i:<4}{a[0]:<10}{a[2]:>8}{a[3]:>16}') # a = para cada dado [0] nome, a[2] para média
while True:
    print('-' * 45)
    opc = int(input('Mostrar notas de qual aluno? (999 para interromper): ')) # opção correspondende ao índice

    if opc <= len(ficha) - 1:  # para que essa opção seja menor que os índice cadastrados
        #len para contar os elementos cadastrados
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
        # na opçao desejada que é o len de ficha ou seja no elemento [1] , [1] = elemento,na ficha posição [0] = nome
        # na ficha posição [1]: notas digitada
    if opc == 999:
        print('Finalizando')  # Finalizar programa
        break
