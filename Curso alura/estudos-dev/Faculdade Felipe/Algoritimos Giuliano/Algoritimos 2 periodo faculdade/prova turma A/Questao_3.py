def calcula_imposto(taxa,custo):
    novo_valor = custo + (custo*(taxa/100))
    return novo_valor

def busca_binaria(lista,chave):
    lista.sort()
    inicio,fim = 0, len(lista)-1
    while inicio <=fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            return meio
        elif chave < lista[meio]:
            fim = meio -1
        else:
            inicio = meio +1
    return - 1

#------------------CHAMANDO CALCULA IMPOSTO-----------------------------
try:
    taxa = float(input('Digite a taxa do imposto: '))
    custo = float(input('Digite o valor do custo em impostos: '))  
    resultado = calcula_imposto(taxa,custo)
    print(resultado)  
except ValueError:
    print('Digite apenas numeros...')
  


#--------------------------------LISTA DE PREÇOS------------------------------- 
valida = False
while not valida:
    try: 
        lista_precos = input('Digite uma lista de preço seperada por virgula com 5 preços: ').split(',')
        valores_inteiro = []
        for valor in lista_precos:
            valores_inteiro.append(float(valor.strip()))  
        if len(valores_inteiro) >=5:
            valida = True
            break
        else:
            print('lista pequena demais')
    except ValueError:
        print('Digite apenas numeros validos')        
print(f'Lista de preços desordenada: {valores_inteiro}')    


#------------------------------------ordenando lista de preços------------------------------
ordenar = sorted(valores_inteiro)
print(f'Lista de preços ordenada: {ordenar}')

#--------------------------------chamando a busca binaria e vendo se encontramos o valor na lista--
busca = busca_binaria(ordenar,resultado)
if busca != -1:
    print(f'O numero {resultado} foi encontrado no indice {busca} da lista de preços')
else:
    print(f'Valor {resultado} nao encontrado na lista {ordenar}')
