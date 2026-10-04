def heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    print(f"\nHeapify no índice {i}, arr: {arr[:n]} (considerando tamanho {n})")

    if esquerda < n and arr[esquerda] > arr[maior]:
        print(f"  Filho esquerdo {arr[esquerda]} > raiz {arr[maior]}")
        maior = esquerda

    if direita < n and arr[direita] > arr[maior]:
        print(f"  Filho direito {arr[direita]} > maior atual {arr[maior]}")
        maior = direita

    if maior != i:
        print(f"  Troca {arr[i]} com {arr[maior]}")
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)
    else:
        print(f"  Raiz no índice {i} já é maior que os filhos.")

def heap_sort(arr):
    n = len(arr)

    print(f"Array inicial: {arr}")

    # Construção do max heap
    for i in range(n // 2 - 1, -1, -1):
        print(f"\nConstruindo heap - chamando heapify para i={i}")
        heapify(arr, n, i)
        print(f"Array após heapify: {arr}")

    # Extração dos elementos do heap
    for i in range(n - 1, 0, -1):
        print(f"\nTrocando raiz {arr[0]} com elemento na posição {i} ({arr[i]})")
        arr[i], arr[0] = arr[0], arr[i]
        print(f"Array após troca: {arr}")
        print(f"Chamando heapify para reestruturar heap até o índice {i}")
        heapify(arr, i, 0)
        print(f"Array após heapify: {arr}")

    print(f"\nArray ordenado: {arr}")

# Teste com exemplo
lista = [4, 10, 3, 5, 1]
heap_sort(lista)
