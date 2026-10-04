def potencia(x,n):
    if n == 0:
        return 1
    else:
        return x* potencia(x,n-1)
numero = int(input('Digite um numero: '))
expoente = int(input('Digite a sua potencia: '))
resultado = potencia(numero,expoente)
print(resultado)    