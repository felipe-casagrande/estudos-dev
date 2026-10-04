estoque = {}
def adicionar_produto():
    produto = {}
    nome_produto = input('Nome do produto:')
    produto['nome'] = nome_produto
    produto['quantidade'] = int(input('quantidade: '))
    produto['preco'] = float(input('preço: '))
    print(f'O produto {nome_produto} foi cadastrado')
    estoque[nome_produto] = produto
    
    menu()



def listar_produto():
    print('LISTA DE PRODUTOS')
    print()
    print(f'{'nome':<20}{'quantidade':<20}{'preço':<20}')
    for item in estoque.values():
        print(f'{item['nome']:<20}{item['quantidade']:<20}{item['preco']:<20}')

    menu()    


def atualizar_quantidade():
    atualizar = input('nome do item a ser atualizado: ')
    nova_quantidade = int(input('nova quantidade: '))
    for item in estoque.values():
        if item['nome'] == atualizar:
            item['quantidade'] = nova_quantidade
            print(f'{item['nome']} atualizado para {nova_quantidade}')
            menu()
        else:
            print('nome não cadastrado')
            return
    menu()    


def remover_produto():
    produto_removido = input('nome do produto a ser removido: ')
    if produto_removido in estoque:
        del estoque[produto_removido]
        print(f'produto {produto_removido} removido')
    menu()        

def sair():
    print('saindo do programa....')

def menu():
    print('Seja bem vindo ao sistema')
    print('O que deseja executar:')
    print('1- Adicionar produto')
    print('2- Listar Produto')
    print('3- Atualizar quantidade')
    print('4- Remover produto')
    print('5- Fechar programa')
    acao = int(input('selecione a opção desejada:'))
    if acao == 1:
        adicionar_produto()
    elif acao == 2:
        listar_produto()
    elif acao == 3:
        atualizar_quantidade()
    elif acao == 4:
        remover_produto()
    elif acao == 5:
        print('saindo...')

menu(
)
