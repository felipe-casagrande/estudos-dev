#Selection Sort percorre toda a lista diversas vezes, buscando o menor número na parte ainda não ordenada. A cada passada, ele seleciona esse menor número e troca com o elemento na posição atual, "retirando" esse valor da lista que ainda precisa ser verificada e passando para o proximo valor

def selection_sort(lista):
    tamanho = len(lista)                            # Obtém o tamanho da lista
    for i in range(tamanho):                           # Loop para percorrer toda a lista
        menor_valor = i                                  # Assume que o menor valor está na posição i
                                                        # Loop para encontrar o menor valor na sublista à direita de i
        for j in range(i + 1, tamanho):                    # vai percorrer a lista da direita toda ate achar um valor menor que o i, caso acho, menor valor passa a ser j
                                                            # Se encontrar um valor menor que o atual menor, atualiza o índice
            if lista[j] < lista[menor_valor]:
                menor_valor = j
        # Troca o elemento na posição i com o menor encontrado
        lista[i], lista[menor_valor] = lista[menor_valor], lista[i]

# Exemplo de uso
numeros = [5, 3, 8, 4, 2]
selection_sort(numeros)  # Ordena a lista usando Selection Sort
print(numeros)  # Imprime a lista ordenada: [2, 3, 4, 5, 8]
