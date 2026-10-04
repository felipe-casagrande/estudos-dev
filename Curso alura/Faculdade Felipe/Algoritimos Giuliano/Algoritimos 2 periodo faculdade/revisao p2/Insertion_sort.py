def insertion_sort(lista):
    tamanho = len(lista)
    for i in range(1,tamanho):
        chave = lista[i]                                    #numero que esta sendo analisado
        j = [i-1]                                           #indice do numero a esquerda, se o i for 4, j vai ser 3
        while j >=0 and lista[j] > chave:               #enquanto o indice for positivo e a chave for menor, continuar analisando, pra ver ate onde a chave vai ser inserida
            lista[j+1] = lista[j]                           # ta avançando de posição pra gerar espaço pro novo numero entrar    
            j -= 1
        lista[j+1]  = chave       # +1 porque todo looping o j perde 1, ent no ultimo looping mesmo nao dando certo ele tb tirou 1 , entao a posiçaao certa é a vanaçando 1 
    return lista        