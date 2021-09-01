frase = str(input('Digite uma frase para verificar: ')).upper()
inverso = frase[:: -1]
print('O Inverso de {} é {} '.format(frase, inverso))
if inverso == frase:
    print('{} é igual a frase digitada, Portando é Palindrome'.format(inverso))
else:
    print('{}  não é igual {} , Portando  não é Palindrome'.format(inverso, frase))
