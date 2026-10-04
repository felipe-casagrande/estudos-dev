def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

valor_a = int(input('Digite o primeiro numero: '))
valor_b = int(input('Digite o segundo numero: '))
resultado = mdc(valor_a,valor_b)
print(f'O maximo divisor comum de {valor_a} e {valor_b} é {resultado}')