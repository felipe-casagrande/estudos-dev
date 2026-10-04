def calcularimposto(taxa, custo):
    return custo + (custo * taxa / 100)

def bubblesort(lista):
    quant = len(lista)
    for c in range(quant):
        for s in range(0, quant - c -1):
            if lista[s] > lista[s + 1]:
                lista[s], lista[s + 1] = lista[s + 1], lista[s]

def binaria(lista, alvo):
    inicio = 0 
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False

try:
    taxa = float(input('Digite a taxa do imposto: '))
    custo = float(input("Digite o custo do produto: "))
    valorimposto = calcularimposto(taxa, custo)
    print(f'Valor com imposto foi: {valorimposto:.2f}')
except ValueError:
    print("Erro: Digite numeros validos.")
    exit()

valida = False
while not valida:
    str = input("Digite 5 preços, com virgula: ")
    try:
        lista = [float(x.strip()) for x in str.split(",")]
        if len(lista) < 5:
            print("Erro. Pelo menos 5 numeros.")
        else:
            valida = True
    except ValueError:
        print("Erro. so numeros validos e com virgula.")
bubblesort(lista)
print('Lista de preços ordenada:')
print(lista)