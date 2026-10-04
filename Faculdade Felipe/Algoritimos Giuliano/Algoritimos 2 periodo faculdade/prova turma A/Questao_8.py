def bubble_sort(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(0,tamanho-1 -i):
            print(f'lista atual: {lista}')
            print(f'comparando o numero {lista[j]} com o numero {lista[j+1]}')
            if lista[j] > lista[j+1]:
                print(f'O numero {lista[j]} é maior que o numero {lista[j+1]}, trocando eles de posição;;')
                lista[j],lista[j+1] = lista[j+1],lista[j]
                print(f'Lista após a troca {lista}')
            else:
                print('nao faz a troca')
lista = [5,2,8,1,9]
bubble_sort(lista)
print(lista)    