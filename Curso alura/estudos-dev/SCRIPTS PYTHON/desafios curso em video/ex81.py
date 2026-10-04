lista = []
while True:
    n = int(input('Digite um numero: '))
    prosseguir = input('Deseja continuar [sim/nao]? ')
    lista.append(n)
    if prosseguir == 'nao':
        break
lista.sort(reverse=True)
print(lista)
print(f'A quantidade de elemento na lista é: {len(lista)}')
if 5 in lista:
    print('O numero 5 está na lista!')
else:
    print('O numero 5 nao esta na lista!')     