agenda = []
def cadastrar_contato(nome,telefone,email):
    contato = {
        'nome':nome,
        'telefone':telefone,
        'email':email
    }
    agenda.append(contato)
def listar_cadastrados():
    print(f'{'nome'} | {'telefone'} | {'email'}')
    for pessoa in agenda:
        print(f'{pessoa['nome']} | {pessoa['telefone']} | {pessoa['email']}')



def busca_nome(nome):
    for pessoa in agenda:
        if pessoa['nome'] == nome:
            print(pessoa)        


def excluir_contato(nome):
    for pessoa in agenda:
        if pessoa['nome'] == nome:
            agenda.remove(pessoa)    


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
            listar_cadastrados()
        elif opcao == 3:
            nome = input('Digite o nome do contato que está buscando: ')
            busca_nome(nome)
        elif opcao == 4:
            nome = input('Digite o nome do contato que você quer excluir: ')
            excluir_contato(nome)
        elif opcao == 5:
            print('Saindo...')
            break

menu()                