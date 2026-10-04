def couting_sort(lista):
    valor_maximo = max(lista)
    contador = [0]* (valor_maximo+1)
    saida = [0] * len(lista)
    for num in lista:
        contador[num] +=1

    for i in range(1,valor_maximo+1):
        contador[i] += contador[i-1]

    for i in reversed(range(len(lista))):
        num = lista[i]
        posicao = contador[num] - 1 
        saida[posicao] = num
        contador[num] -=1
    
    return saida











































'''def counting_sort_clean(A):
    k = max(A)
    n = len(A)
    
    C = [0] * (k +1)
    B = [0] * n

    # Etapa 1: Contar ocorrências
    for num in A:
        C[num - 1] += 1
    print("Array C após contagem:    ", C)
    
    # Etapa 2: Soma acumulada
    for i in range(1, k):
        C[i] += C[i - 1]
    print("Array C acumulativo:      ", C)
    
    # Etapa 3: Construir array B ordenado
    for i in reversed(range(n)):
        num = A[i]
        pos = num - 1
        B[C[pos] - 1] = num
        C[pos] -= 1
    
    return B

# Teste
A = [3, 2, 4, 7, 4, 7, 1, 2, 3]
print("Array A original:         ", A)
resultado = counting_sort_clean(A)
print("Array B ordenado (final): ", resultado)'''
