import pandas as pd
from adicionar_credenciais import gerar

print('******************************')
print('*****Gerenciador de senha*****')
print('******************************')


def comecar():
    selecao = input('O que deseja fazer?: \n 0 - Ver emails e senhas \n 1 - Criar email e senha \n 2 - Fechar \n : ')

    if selecao == '0':
        dados = pd.read_csv('gerenciador.csv')
        print(dados)
        comecar()
    elif selecao == '1':
        gerar()
        comecar()
    elif selecao == '2':
        print('Encerrado!')
    else:
        print('Erro!')

    print('__*__')


comecar()
