def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar(lista):
    primos = []
    for n in lista:
        if primo(n):
            primos.append(n)
    return primos

original = list(range(1, 1001))
listaprimos = filtrar(original)

print("Numeros primos de 1 á 1000: ")
print(listaprimos)