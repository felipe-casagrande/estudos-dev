Deposito= ()

def adicionar_produto(Deposito,codigo,nome,quantidade,preco):
    for item in Deposito:
        if item['codigo'] == codigo:
            return Deposito # sem alteração
        
    produtos = {'codigo': codigo, 'nome': nome, 'quantidade': quantidade, 'preco': preco}
    Deposito += (produtos,)
    return Deposito

def atualizar_quantidade(Deposito,codigo,nova_quantidade):
    Deposito = tuple(
        {**item, 'quantidade': nova_quantidade } if item['codigo'] == codigo else item  #leitura: para cada item do deposito, se a chave codigo for igual ao parametro que passei, ele vai copiar todo o dicionario, e vai atualizar o valor da chave  quantidade para a nova quantidade
        for item in Deposito
    )


















 #Estoque = {}

# def adicionar_produto(codigo, nome, quantidade, preco):
#     Estoque[codigo] = (codigo, nome, quantidade, preco)

# def atualizar_quantidade(codigo, nova_quantidade):
#     if codigo in Estoque:
#         _, nome, _, preco = Estoque[codigo]
#         Estoque[codigo] = (codigo, nome, nova_quantidade, preco)

# def produtos_disponiveis():
#     return ','.join(item[1] for item in Estoque.values() if item[2] > 0)

# def produtos_indisponiveis():
#     return ','.join(item[1] for item in Estoque.values() if item[2] <= 0)

# def valor_estoque():
#     return sum(item[2] * item[3] for item in Estoque.values())