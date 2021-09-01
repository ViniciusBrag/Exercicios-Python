from ex113.dados import *
from ex115.Lib.Arquivo import *

arq = 'DadosPessoas.txt'
if not arquiexist(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ').title()
        idade = leiaint('Idade: ')
        cadastrararq(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...Muito Obrigado')
        break
    else:
        print('\033[31mError! Digite um opção válida\033[31m')

