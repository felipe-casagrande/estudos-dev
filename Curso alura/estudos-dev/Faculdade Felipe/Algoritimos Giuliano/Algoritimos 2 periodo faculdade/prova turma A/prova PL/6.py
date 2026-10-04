def bubblesort(lista):
    n = len(lista)
    for i in range(n):
        troca = False
        print(f'PAssagem {i + 1}: ')
        for j in range(n - i - 1):
            print(f"COmprando {lista[j]} e {lista[j + 1]}")
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                troca = True
        print("Lista:", lista)
        if not troca:
            print("Sem troca de passagem.")
            break
lista = [7, 2, 4, 1, 8, 5, 3]
print("Lista inicial: ", lista)
bubblesort(lista)
print("Lista Final: ", lista)
