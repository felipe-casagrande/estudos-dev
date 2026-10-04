def contagem(numero):
    for c in range(numero+1):
        for s in range(c):
            print(c, end=' ')
        print()    


numero = int(input('Digite um numero'))
resultado = contagem(numero)
