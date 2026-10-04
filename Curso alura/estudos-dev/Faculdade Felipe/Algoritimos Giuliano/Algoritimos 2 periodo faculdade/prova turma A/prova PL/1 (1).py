vetor = [1,2,3,4,5,6,7,8,9,10]

def vetorinvertido(vetor):
    vetorinvertido = []
    for i in range(len(vetor)-1,-1,-1):
        vetorinvertido.append(vetor[i])

    for numero in vetorinvertido:
        print(numero)

vetorinvertido(vetor)
