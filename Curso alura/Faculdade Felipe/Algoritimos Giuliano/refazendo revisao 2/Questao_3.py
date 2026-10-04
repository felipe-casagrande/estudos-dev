estoque = []
def adicionar_produto(nome,quantidade):
    for item in estoque:
        if item['nome'] == nome:
            print('Produto ja cadastrado')
            return
    produto = {
        'nome':nome,
        'quantidade':quantidade
    }
    estoque.append(produto)


def listar_produtos():
    print('PRODUTOS CADASTRADOS')
    print(f'{'Produto: ':<15} | {'quantidade':<15}')
    for produto in estoque:
        print(f'{produto['nome']:<15} | {produto['quantidade']:<15}')
        
def atualizar_quantidade(nome,nova_quantidade):
    for item in estoque:
        if item['nome'] == nome:
            item['quantidade'] = nova_quantidade

def remover_produto(nome):
    for item in estoque:
        if item['nome'] == nome:
            estoque.remove(item)




def menu():
    while True:
        opcao = int(input('Digite a opção desejada: '))    
        if opcao == 1:
            nome = input('Digite o nome do produto: ')
            quantidade = int(input('Digite a quantidade no estoque: '))
            adicionar_produto(nome,quantidade)
        elif opcao == 2:
            listar_produtos()

        elif opcao == 3:
            nome = input('Digite o nome do produto que quer atualzar: ')
            nova_quantidade = int(input('Digite a nova quantidade: '))
            atualizar_quantidade(nome,nova_quantidade)
        elif opcao == 4:
            nome = input('Digite o nome do produto a ser removido: ')
            remover_produto(nome)
        elif opcao == 5:
            print('saindo...')
            break

menu()        
