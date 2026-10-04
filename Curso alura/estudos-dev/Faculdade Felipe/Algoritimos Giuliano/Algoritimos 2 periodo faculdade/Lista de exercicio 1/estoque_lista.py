'''Versão 2: Uma loja deseja gerenciar seu estoque de produtos de forma eficiente. Para isso, 
    precisa de um sistema que utilize dicionários e tuplas para armazenar informações sobre os 
    produtos. 
    Cada produto tem: 
    • Código (único) 
    • Nome 
    • Quantidade disponível 
    • Preço unitário 
    O sistema deve permitir: 
    1. Adicionar novos produtos ao estoque. 
    2. Atualizar a quantidade de um produto existente. 
    3. Listar todos os produtos disponíveis. 
    4. Calcular o valor total do estoque. '''


    #fiz a versao 2

Estoque = []


def adicionar_produto(codigo,nome,quantidade,preco):
        for item in Estoque:
            if item['codigo'] == codigo:
                print(f'Já existe um produto com o codigo {codigo}')
                return #nao coloquei nada pra retornar pra justamente nao adicionar nada pois o codigo esta repetido

        produto = {}
        produto['codigo'] = codigo
        produto['nome'] = nome
        produto['quantidade'] = quantidade
        produto['preco'] = preco
        Estoque.append(produto)    




    # essa função vai percorrer o minha lista e acessar o dicionario, se o codigo for igual o escolhido, ele acessa o dicionario e muda, se n for ela passa pro proximo até encontrar o codigo
def atualizar_quantidade(codigo, nova_quantidade):
        for item in Estoque:
            if item['codigo'] == codigo:
                item['quantidade'] = nova_quantidade
                print(f'Quantidade de {item['nome']} foi atualizado para {nova_quantidade}')
                exibir_estoque()    #coloquei aqui para toda vez que atualizar uma quantidade, passar o estoque novamente, pra ficar bonitinho


    #nessa função listar irei colocar apenas o nome do prouduto disponivel, espero que esteja correto.

def produtos_disponiveis():
        disponiveis = []
        for item in Estoque:      
            if item['quantidade']  > 0:
                disponiveis.append(item['nome'])
        return ', '.join(disponiveis)   # para sair em forma de string e nao de lista



    #criei uma variavel que percorre cada dicionario na lista, fazendo a conta de preço x quantidade para saber o valor total do estoque.
def calcular_valor():
        valor = 0
        for item in Estoque:
            valor += item['preco'] * item['quantidade']
        return valor
        

def exibir_estoque():
        print('                     ESTOQUE ATUAL:'                         )
        print()
        print(f'{'Código':<10}{'Nome':<20}{'quantidade':<12}{'preço':<12}')
        print('-'*50)
        for item in Estoque:
            print(f'{item['codigo']:<10}{item['nome']:<20}{item['quantidade']:<12}R$:{item['preco']:<12}')



adicionar_produto(11,'HP', 3, 10)    
adicionar_produto(13,'not', 2, 2)

exibir_estoque()

atualizar_quantidade(11,5)
produtos_disponiveis()
disponiveis = produtos_disponiveis()
print(f'Itens disponiveis: {disponiveis}')


calcular_valor()
calculo = calcular_valor()
print(f'Valor geral do estoque é: R${calculo}')
