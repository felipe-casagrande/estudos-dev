#criar uma lista de 5 valores e que cada valor seja adicionado em ordem crescente
lista = []
for c in range(0,5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('fim')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos +=1
print(lista)