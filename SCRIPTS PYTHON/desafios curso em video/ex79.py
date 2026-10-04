lista = []

while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor invalido')
    seguir = input('Desaja continuar S/N? ') 
    if seguir == 'nao':
        break
print(lista)  
    