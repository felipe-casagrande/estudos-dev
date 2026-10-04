"""
Radix Sort - ordena números inteiros analisando um dígito por vez, da casa menos significativa para a mais significativa.
Usa um método estável de ordenação (base_radix) para garantir que a ordem dos números iguais seja preservada.

Dúvidas avançadas abordadas aqui:
- Por que usamos 'count[index] - 1' ao definir a posição no output?  
  A contagem cumulativa indica a posição *final* (1-based) para os elementos com aquele dígito.
  Como os índices em Python são 0-based, subtraímos 1 para obter o índice correto no array.
- Por que percorremos a lista do fim para o início no while?  
  Isso mantém a estabilidade da ordenação, ou seja, para números com o mesmo dígito, a ordem original é preservada.
- O que significa o cálculo 'index = (lista[i] // exp) % 10'?  
  Ele extrai o dígito na posição atual (unidades, dezenas, centenas, etc) usando divisão inteira e módulo 10.
- Por que o loop while só termina quando 'maximo // exp' é zero?  
  Porque quando o maior número dividido por exp dá zero, não existem mais dígitos para processar.
"""

def base_radix(lista, exp):
    tamanho_lista = len(lista)
    output = [0] * tamanho_lista          # Array temporário para armazenar os números ordenados neste passo
    count = [0] * 10                      # Contador para os dígitos de 0 a 9

    # Contar a frequência de cada dígito na posição exp
    for i in range(tamanho_lista):
        index = (lista[i] // exp) % 10   # Extrai o dígito relevante
        count[index] += 1

    # Modifica count para armazenar posições finais cumulativas dos dígitos
    # Isso significa que count[i] agora representa a posição final (1-based) no output dos números com dígito i
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir o array output de trás para frente para manter a estabilidade
    i = tamanho_lista - 1
    while i >= 0:
        index = (lista[i] // exp) % 10
        posicao = count[index] - 1         # Ajusta para índice 0-based do Python
        output[posicao] = lista[i]         # Coloca o número na posição correta do output
        count[index] -= 1                  # Atualiza para próxima posição livre do dígito
        i -= 1

    # Copia o resultado de output para a lista original, para o próximo passo do Radix Sort
    for i in range(tamanho_lista):
        lista[i] = output[i]

def radix_sort(lista):
    maximo = max(lista)                    # Maior valor para determinar quantas casas analisar
    exp = 1                               # Começamos pelas unidades (10^0)
    while maximo // exp > 0:              # Enquanto existirem dígitos para processar
        base_radix(lista, exp)            # Ordena baseado no dígito atual
        exp *= 10                        # Passa para a próxima casa decimal

# Teste
arr = [170, 45, 75, 90, 802, 24, 2, 66]        
radix_sort(arr)
print(arr)
