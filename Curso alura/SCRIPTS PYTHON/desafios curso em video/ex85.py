lista = [[],[]]

for c in range(1,8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
         lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os pares são: {lista[0]}')
print('->'*30)
print(f'Os impares sao: {lista[1]}')