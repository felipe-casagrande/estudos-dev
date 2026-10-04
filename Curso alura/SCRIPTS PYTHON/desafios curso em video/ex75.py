
numeros = (int(input('Digite um numero: ')),
           int(input('Digite um numero: ')),
           int(input('Digite um numero: ')),
           int(input('Digite um numero: ')))
 

print(f'A quantidade de numeros 9 é: {numeros.count(9)}')
if 3 in numeros:
    print(f'O numero 3 aparece pela primeira vez na posição: {numeros.index(3)}')
else:
    print('O valor 3 nao tem na nossa sequencia')
print('Os valores pares são: ', end='')
for n in numeros:

    if n % 2 == 0:
        print(n, end=' ')