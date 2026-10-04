def soma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + soma_digitos(n // 10)
numero = int(input('Digite um numero e te direi a soma deles: '))
resultado = soma_digitos(numero)
print(resultado)