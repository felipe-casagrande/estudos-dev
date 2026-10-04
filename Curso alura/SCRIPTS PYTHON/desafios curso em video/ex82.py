lista = []
lista_par = []
lista_impar = []
while True :
    n =int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    seguir = input('Deseja seguir [sim/nao]? ')
    if seguir == 'nao':
        break
print(f'{lista}\n{lista_par}\n{lista_impar}')
