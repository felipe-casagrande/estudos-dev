def busca_binaria(lista,chave):
    lista.sort()
    inicio, fim = 0, len(lista) -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            return meio
        elif chave < lista[meio]:
            fim = meio -1  
        else:
            inicio = meio + 1
    return -1
lista = [10,20,30,40]
chave = int(input('qual o numero que deseja buscar?'))
busca = busca_binaria(lista,chave)
if busca != -1:
    print(f'O numero {chave} foi encontrado na posição {busca}')
else:
    print(f'O número {chave} não foi encontrado.')
