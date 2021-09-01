from time import sleep
def maior(* num):
    cont = maiores = 0
    print('-=' * 30)
    print('Analisando os valores...')
    for valores in num:
        print(valores, end=' ', flush=True)
        sleep(0.2)
        if cont == 0:
            maiores = valores
        else:
            if valores > maiores:
                maiores = valores
        cont += 1
    print(f'Fora analisados {cont} números. \n O maior é o número {maiores}')
#programa principal
maior(1, 5, 7, 9, 10)
maior(2, 5, 6, 9, 11)
maior(4, 8, 1)
maior(2, 6, 2)
maior(0)
maior()