import pandas as pd
from adicionar_credenciais import gerar, deletar_email

print('******************************')
print('*****Gerenciador de senha*****')
print('******************************')


def comecar():
    selecao = input('O que deseja fazer?: \n 0 - Ver emails \n 1 - Criar email e senha \n 2 - Deletar email  \n q - Fechar\n: ')

    if selecao == '0':
        dados = pd.read_csv('gerenciador.csv')
        print(dados)
        print('___*___')
        comecar()
    elif selecao == '1':
        gerar()
        comecar()
    elif selecao == '2':
        deletar_email()
        comecar()
    elif selecao == 'q':
        print('Encerrado!')
    else:
        print('Erro!')

    print('__*__')


comecar()
