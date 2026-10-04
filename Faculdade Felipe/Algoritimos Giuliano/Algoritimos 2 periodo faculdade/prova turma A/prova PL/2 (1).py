def impressaopadrao(n):
    for c in range(1, n + 1):
        for s in range(c):
            print(c, end=' ')
        print()

numero = int(input("Digite um numero inteiro: "))
impressaopadrao(numero)
