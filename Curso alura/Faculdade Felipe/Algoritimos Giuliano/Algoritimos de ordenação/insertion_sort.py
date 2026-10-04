#"O Insertion Sort ordena começando do segundo elemento e compara com a sublista da esquerda (que já está ordenada), movendo os elementos maiores para a direita até encontrar a posição correta para inserir a chave.



def insertion_sort(lista):
    tamanho = len(lista)
    for i in range(1,tamanho):      #1 para começar do segundo elemento do indice, e começar a comparação do segundo x o primeiro
        chave = lista[i]           #valor que queremos inserir 
        j = i - 1                   #elemento anterior que esta sendo comparado
        while j>=0 and lista[j] > chave:
            lista[j+1]= lista[j]           #basicamente, enquanto o valor anterior for maior que a chave, continuamos o loop, faz j -= 1 para percorrer o indice anterior novamente, ate achar uma posição.
            j -=1
        lista[j+1] = chave                 # inserindo a chave no lugar correto, como ja demos -1 anteriormente, temos que dar +1 para garantir que ela vá para o lugar correto
    return lista

lista = [10,20,4,3,5,15]
ordenado = insertion_sort(lista)
print(ordenado)        