palavras = ('Letras',
            'vogais',
            'aprender',
            'programar',
            'python',
            'java',
            'engenharia de software',
            'assembly',
            'javascript',
            'node')
for p in palavras:
    print(f' \n Na palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')