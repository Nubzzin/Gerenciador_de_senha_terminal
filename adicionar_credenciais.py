import random
import string
import pandas as pd

class Email:
    def __init__(self,titulo,email):
        self.titulo = titulo
        self.email = email
        self.senha = ''

    def gerar_senha(self):
        selecao = input(f'Deseja inserir a senha manualmente(1) ou gerar uma aleatoria(2)?\n(1/2): ')
        if selecao == '1':
            self.senha = input('Digite a senha: ')
            
        elif selecao == '2':
            tamanho_senha = int(input('Qual o tamanho da senha?: '))
            lista = []

            for i in range(tamanho_senha):
                lista.append(random.choice(string.ascii_letters + string.digits))
                self.senha = ''.join(map(str, lista))
    

def gerar():
    dados = pd.read_csv('gerenciador.csv')

    titulo = input('Qual o titulo do email?: ').title()
    email = input('Qual o email?: ')
    usuario = Email(titulo,email)
    senha = usuario.gerar_senha()

    print(f'Essas são suas informações:\
          \nTitulo: {usuario.titulo}\
          \nEmail: {usuario.email}\
          \nSenha: {usuario.senha}')
    cin = input('Deseja confirmar?(s/n): ')

    if cin == 's':
        adicionar = pd.DataFrame({'Titulo': [usuario.titulo], 'Email': [usuario.email], 'Senha': [usuario.senha]})
        dados = pd.concat([dados,adicionar],ignore_index=True)
        dados.to_csv('gerenciador.csv',index=False)
        print(dados)

def deletar_email():
    dados = pd.read_csv('gerenciador.csv')

    print('Qual email deseja excluir?')
    print(dados)
    selecao = int(input('__\ndigite o numero referente a exclusão desejada:'))
    confirmacao = input('Tem certeza?:(s/n) ')
    if confirmacao == 's':
        dados = dados.drop(selecao)
        dados.to_csv('gerenciador.csv',index=False)
    elif confirmacao == 'n':
        print('Não confirmado')

if __name__ == '__main__':
    gerar()
    deletar_email()
