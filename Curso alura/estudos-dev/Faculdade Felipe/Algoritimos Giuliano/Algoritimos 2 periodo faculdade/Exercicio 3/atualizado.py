'''lista de comandos
any()- serve para comparar, nesse codigo ele compara se minha variavel nome é igual ao item['nome'] em algum momento
'''

estoque = []

def adicionar_produto(nome,quantidade,preco):
    produto = {
    'nome': nome,
    'quantidade': quantidade,
    'preco': preco
    }
    estoque.append(produto)
    print(f'Produto {nome} adicionado! ')
    return menu()

def listar_produtos():
    print(f'{'nome':<20}{'quantidade':<20}{'preço':<20}')
    for item in estoque:
        print(f'{item['nome']:<20}{item['quantidade']:<20}R${item['preco']:<20}')
    return menu()    

def atualizar_quantidade(nome,nova_quantidade):
    for item in estoque:
        if item['nome'] == nome:
            item['quantidade'] = nova_quantidade
            print(f'Nova quantidade de {item['nome']} foi atualizada para {nova_quantidade}')
    return menu()

def remover_produto(nome):
    for item in estoque:
        if item['nome'] == nome:
            print(f'Produto {item['nome']} foi removido do sistema..')
            estoque.remove(item)
            menu()
def sair():
    print('saindo...')
    

def menu():
    print()
    print('Seja bem vindo ao sistema')
    print('-'*30)
    print('1- Adicionar produto')
    print('2- Listar produtos')
    print('3- Atualizar quantidade')
    print('4- Remover produto')
    print('5- sair')
    escolha = int(input('O que deseja: '))
    if escolha == 1:
        nome = str(input('Digite o nome do produto: '))
        if any(item['nome'] == nome for item in estoque):    # Se le basicamente:  Se item['nome'] for igual nome em igual momento da iteração, ele vai mostrar cadastrado
            print('produto já cadastrado..')
            return menu()
        quantidade = int(input('Digite a quantidade: '))
        preco = float(input('Digite o preço do produto: '))
        adicionar_produto(nome,quantidade,preco)

    elif escolha == 2:
        listar_produtos()

    elif escolha == 3: 
        nome = str(input('Nome do produto a ser atualizado: '))
        if not any(item['nome'] == nome for item in estoque):  # Verifica se o nome está no estoque
            print('Produto não encontrado')
            return menu()
        nova_quantidade = int(input('Digite a nova quantidade: '))
        atualizar_quantidade(nome,nova_quantidade)
        menu()
    
    elif escolha == 4:
        nome = str(input('Nome do produto a ser removido: '))
        if not any(item['nome'] == nome for item in estoque):
            print('Produto nao encotrado')
            return menu()
        remover_produto(nome)
    
    elif escolha == 5:
        sair()
        

menu()