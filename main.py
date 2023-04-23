import pandas as pd
from adicionar_credenciais import gerar,deletar_email, Email

print('******************************')
print('*****Gerenciador de senha*****')
print('******************************')

def comecar():
    selecao = input('O que deseja fazer?: \n 0 - Ver emails \n 1 - Criar email e senha\n 2 - Deletar email\n: ')

    if selecao == '0':
        dados = pd.read_csv('gerenciador.csv')
        print(dados)
        print('___*___')

    elif selecao == '1':
        gerar()
    elif selecao == '2':
        deletar_email()
    else:
        print('Erro! Tente as alternativas disponiveis!')

    print('__*__')

while True:
    comecar()