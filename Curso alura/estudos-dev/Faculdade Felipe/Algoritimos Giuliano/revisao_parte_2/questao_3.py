''' Implemente um programa para gerenciar o estoque de uma pequena loja. O sistema deve 
permitir:
1. Adicionar um novo produto com nome e quantidade.
2. Listar todos os produtos com suas respectivas quantidades.
3. Atualizar o estoque de um produto (aumentar ou reduzir quantidade).
4. Remover um produto do sistema.
Utilize dicionários para armazenar os dados.'''
estoque = []
def adicionar_produto(nome,quantidade):
    for item in estoque:
        if item['produto'] == nome:
            print('Este produto já está cadastrado')
            return -1
    produto = {
        'produto':nome,
        'quantidade': quantidade
    }
    estoque.append(produto)
    print(f'Produto {nome} cadastrado!')

def listar_produto():
    for produto in estoque:
        print(f'Produto: {produto['produto']} | quantidade {produto['quantidade']}')


def atualizar_quantidade(nome,nova_quantidade):
    for produto in estoque:
        if produto['produto'] == nome:
            produto['quantidade'] = nova_quantidade
            print(f'Quantidade atualizada para {nova_quantidade}')        

def menu():
    print('Digite 1 para cadastrar produto')
    print('Digite 2 para exibir todos os produtos')
    print('Digite 3 para atualizar quantidade')
    print('Digite 4 para sair')
    while True:
        opcao = int(input('Qual opção deseja: '))
        if opcao == 1:
            nome = input('Digite o nome do produto: ')
            quantidade = int(input('Digite a quantidade do produto: '))
            adicionar_produto(nome,quantidade)
        elif opcao == 2:
            listar_produto()
        elif opcao == 3:
            nome = input('Nome do item que será atualizado: ')
            nova_quantidade = int(input('Digite a nova quantidade: '))
            atualizar_quantidade(nome,nova_quantidade)
        elif opcao == 4:
            print('Encerrando')
            break

menu()        