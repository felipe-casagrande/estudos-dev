def bubblesort(lista): # aqui começamos a função do bubblesort
    n = len(lista)
    for i in range(n - 1):
        print(f"Passagem {i + 1}: ")
        for j in range(n - i - 1):
            print(f"Comprando {lista[j]} e {lista[j + 1]}", end="") # Nesa área toda estamos trocando os numero lado a lado com o bubblesort
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(f"Trocou: {lista}")
            else:
                print("Não trocou.") # caso ele nao tenha trocado 
        print(f"Lista depois da passagem {i + 1}: {lista}")

numeros = input("Digite a Lista: ")
numeros = [int(num) for num in numeros.split()]
bubblesort(numeros)
print("Lista ordenada: ", numeros)