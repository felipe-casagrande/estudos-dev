lista = []
numero = int(input('Digite um numero e te direi se ele é perfeito: '))
for c in range(numero):
    if numero % (c+1) == 0:
        lista.append(c+1)
        print(lista)
lista.remove(lista[-1])
print(lista)
if sum(lista) == numero:
    print('é perfeito')
else:
    print('nao é perfeito')       