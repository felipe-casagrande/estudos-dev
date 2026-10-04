''''Crie um sistema de agenda em Python que permita:
1. Cadastrar contatos com nome, telefone e e-mail.
2. Listar todos os contatos cadastrados.
3. Buscar um contato pelo nome.
4. Excluir um contato.
Os dados devem ser armazenados em uma lista de dicionários.
'''

agenda = []
def cadastrar_contato(nome,telefone,email):
    contato = {
        'nome':nome,
        'telefone':telefone,
        'email':email
    }
    agenda.append(contato)


def exibir_contato():
    print('Contatos cadastrados!')
    for pessoas in agenda:
        print(f'Nome: {pessoas['nome']} | telefone: {pessoas['telefone']} | email: {pessoas['email']}')    


def contato_especifico(nome):
    for pessoas in agenda:
        if pessoas['nome']== nome:
            print('O contato que você mencionou é:')
            print(f'Nome: {pessoas['nome']} | telefone: {pessoas['telefone']} | email: {pessoas['email']}')        

def excluir_contato(nome):
    for pessoas in agenda:
        if pessoas['nome'] == nome:
            agenda.remove(pessoas)
            print(f'{pessoas['nome']} foi removido da agenda')

def menu():
    print('Digite 1 para cadastrar contatos')
    print('Digite 2 para exibir a lista de contatos')
    print('Digite 3 para pesquisar um contato especifico')
    print('Digite 4 para excluir um contato')
    print('Digite 5 para encerrar o programa')
    while True:
        opcao = int(input('Digite uma opção: '))
        if opcao == 1:
            nome = input('Digite o nome do contato: ')
            telefone = input('Digite o numero do contato')
            email = input('Digite o email: ')
            cadastrar_contato(nome,telefone,email)
        elif opcao == 2:
            exibir_contato()
        elif opcao == 3:
            nome = input('Digite o nome do contato que está buscando: ')
            contato_especifico(nome)
        elif opcao == 4:
            nome = input('Digite o nome do contato que você quer excluir: ')
            excluir_contato(nome)
        elif opcao == 5:
            print('Saindo...')
            break

menu()        