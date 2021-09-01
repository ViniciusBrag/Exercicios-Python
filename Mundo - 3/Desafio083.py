expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0: # que a pilha não está vazia, cada vez que o abre o '(' necessita fecha o ')' entao cada vez que encontrar um ')' ele vai retirar um '(' da pilha
            pilha.pop() # remova o último elemento
        else:
            pilha.append(')') # teve mais parenteses fechando do que abrindo
            break
if len(pilha) == 0: # quaando
    print('Sua expressão está valida')
else:
    print('Sua expressão inválida')
