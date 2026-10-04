def busca_sequencial(lista,chave):
    indice = 0
    for numero in lista:
        if numero == chave:
            return indice
        indice += 1  
    return - 1
        
            
lista = [10,20,30,40]            
chave = int(input('qual o numero deseja buscar?'))
busca = busca_sequencial(lista, chave)

if busca != -1:
    print(f'O número foi {chave} foi encontrado no indice {busca}')
            
else:
    print(f'Número {chave} não encontrado')