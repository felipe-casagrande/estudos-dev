def calcular_graus(celsius):
    fah = (celsius *  9/5) +32
    kelvin = celsius +273.15
    return f'A temperatura em celsius é de {celsius}, fahrenheeit{fah} e em kelvin {kelvin}'

resultado = calcular_graus(10)
print(resultado)