'''Versão 2: Uma loja deseja gerenciar seu estoque de produtos de forma eficiente. Para isso, 
    precisa de um sistema que utilize dicionários e listas para armazenar informações sobre os 
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

Estoque = []
def adicionar_produto(codigo,nome,quantidade,preco):
    produtos={}
    produtos['codigo'] = codigo
    produtos['nome'] = nome
    produtos['quantidade'] = quantidade
    produtos['preco'] = preco
    Estoque.append(produtos)

def atualizar_quantidade(codigo,nova_quantidade):
    for item in Estoque:
        if item['codigo'] == codigo:
            item['quantidade']= nova_quantidade
        else:
            return
        
def produtos_disponiveis():
    disponiveis = []
    for item in Estoque:
        if item['quantidade'] > 0:
            disponiveis.append(item['nome'])
    return ','.join(disponiveis)  



def produtos_indisponiveis():
    indisponiveis = []
    for item in Estoque:
        if item['quantidade'] <= 0:
            indisponiveis.append(item['nome'])
    return ','.join(indisponiveis)        
        
def valor_estoque():
    valor = 0
    for item in Estoque:
        valor += item['preco'] * item['quantidade']
    return valor

def exibir_estoque():
    print('                                  Estoque Atual'                                             )
    print()
    print(f'{'codigo ':<10}{'nome ':<20}{'quantidade ':<12}{'preço':<10}')
    print('-'*100)
    for item in Estoque:
        print(f'{item['codigo']:<10}{item['nome']:<20}{item['quantidade']:<12}R$ {item['preco']:<10}')


adicionar_produto(11,'caderno',3,5)
#adicionar_produto(2,'tijolo',0,5)
#atualizar_quantidade(11,10)
disponiveis = produtos_disponiveis()
indisponiveis= produtos_indisponiveis()
valor = valor_estoque()
print(valor)
print(f'produtos disponiveis: {disponiveis}')
print(f'produtos indisponiveis: {indisponiveis}')
exibir_estoque()
 


