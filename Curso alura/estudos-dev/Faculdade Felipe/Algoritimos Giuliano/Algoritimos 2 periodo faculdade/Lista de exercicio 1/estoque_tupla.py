#versao 1
Estoque = ()


def adicionar_produto(estoque, codigo, nome, quantidade, preco):
    for item in estoque:
        if item['codigo'] == codigo:
            print(f'Já existe um produto com o codigo {codigo}')
            return estoque
    
    produto = {'codigo': codigo, 'nome': nome, 'quantidade': quantidade, 'preco': preco}
    estoque += (produto,)  # Adiciona o dicionário à tupla (recria a tupla)
    return estoque 


def atualizar_quantidade(estoque, codigo, nova_quantidade):
    estoque = tuple(
        {**item, 'quantidade': nova_quantidade} if item['codigo'] == codigo else item    # ** serve para copiar todo o dicionario, e depois só colocar a chave que quero alterar

        for item in estoque
    )
    print(f'Quantidade do produto {codigo} foi atualizada para {nova_quantidade}')
    exibir_estoque(estoque)
    return estoque  


def produtos_disponiveis(estoque):
    disponiveis = []
    for item in estoque:
        if item['quantidade'] > 0:  
            disponiveis.append(item['nome'])
    return ', '.join(disponiveis)

def calcular_valor(estoque):
    valor = 0
    for item in estoque:
        valor += item['preco'] * item['quantidade']
    return valor


def exibir_estoque(estoque):
    print('                     ESTOQUE ATUAL:'                                             )
    print()
    print(f'{"Código":<10}{"Nome":<20}{"Quantidade":<12}{"Preço":<12}')
    print('-'*50)
    for item in estoque:
        print(f'{item["codigo"]:<10}{item["nome"]:<20}{item["quantidade"]:<12}R$:{item["preco"]:<12}')



Estoque = adicionar_produto(Estoque,20,'moto', 2,5)
Estoque = adicionar_produto(Estoque,10,'carro', 1,5)

exibir_estoque(Estoque)

calculo = calcular_valor(Estoque)
disponiveis = produtos_disponiveis(Estoque)
atualizar_quantidade(Estoque,20,4)
print(f'Os produtos disponiveis são: {disponiveis}')
print(f'O valor geral do estoque é R${calculo}')