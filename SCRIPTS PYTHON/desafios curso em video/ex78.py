#ex78
lista = []
for c in range(0,4):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(lista)

print(f'O maior item da lista é: {(max(lista))}, se encontra na posição {lista.index(max(lista))}')
print(f'O menor item da lista é: {(min(lista))}, se encontra na posição {lista.index(min(lista))}')