#bubble sort ordena olhando de par em par


def bubble_sort(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(0,tamanho-1 -i):                   #serve para nao ir ate o ultimo indice, ja que compara de par em par, o ultimo ja seria visto no penultimo
            if lista[j] > lista[j+1]:                       #se o valor que vem antes for maior do que o que vem depois, trocar de posição
                lista[j],lista[j+1] = lista[j+1],lista[j]
numeros = [5, 3, 8, 4, 2]
bubble_sort(numeros)
print(numeros)  
 
            