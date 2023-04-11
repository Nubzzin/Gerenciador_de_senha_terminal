import random
import string
import pandas as pd


def gerar():
    def gerar_titulo():
        titulo = input(f'Qual o titulo do email?: ').title()
        return titulo

    def gerar_email():
        email = input('Qual email deseja criar?: ').lower()
        return email

    def gerar_senha():
        i = input('Quer 0 - criar uma senha ou 1 - senha aleatoria?(0/1): ')
        if i == '0':
            senha = input('Digite sua senha: ')
        elif i == '1':
            tamanho_senha = int(input('Qual o tamanho da senha?: '))
            lista = []

            for i in range(tamanho_senha):
                lista.append(random.choice(string.ascii_letters + string.digits))
                senha = ''.join(map(str, lista))
        else:
            print('Error')
            gerar_senha()

        return senha

    def confirmacao_de_dados(titulo, email, senha):
        dados = pd.read_csv('gerenciador.csv')
        confirmacao = input(
            f'Seu titulo é {titulo} \nSeu email é: {email} \nSua senha é: {senha} \nDeseja confirmar? (S/N): ').lower()

        if confirmacao == 's':
            print('Confirmado!')
            adicionar = pd.DataFrame({'Titulo': [titulo], 'Email': [email], 'Senha': [senha]})
            dados = pd.concat([dados, adicionar], ignore_index=True)
            dados.to_csv('gerenciador.csv', index=False)
        elif confirmacao == 'n':
            print('Não confirmado!')
        else:
            print('Erro! \nTente Sim/Não')
            confirmacao_de_dados(titulo, email, senha)

    confirmacao_de_dados(gerar_titulo(), gerar_email(), gerar_senha())

def deletar_email():
    dados = pd.read_csv('gerenciador.csv')

    print('Qual email deseja excluir?')
    print(dados)
    selecao = int(input('__\ndigite o numero referente a exclusão desejada:'))

    dados = dados.drop(selecao)
    dados.to_csv('gerenciador.csv',index=False) 

if __name__ == '__main__':
    gerar()
    deletar_email()