

def votacao(nasc=0):
    from datetime import date
    anos = date.today().year - nasc
    if anos > 18:
        return (f' com {anos} anos: VOTAÇÃO OBRIGATÓRIA')
    elif anos < 16:
        return (f'com {anos} anos: VOTAÇÃO NEGADA')
    elif anos > 65:
        return (f'com {anos} anos? VOTAÇÃO OPCIONAL')



#programa principal

nome = str(input('Qual o seu nome? '))
ano = int(input('Em que ano você nasceu? '))
votacao(ano)
print(votacao(ano))