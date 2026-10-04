def bubble_sort(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(0,tamanho-1 -i):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
lista = [7,2,4,1,8,5,3]
bubble_sort(lista)
print(lista)    