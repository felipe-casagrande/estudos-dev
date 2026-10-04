def temperatura():
    celsius = float(input('digite o valor em graus: '))
    resultado_fah = (celsius*9/5) + 32
    resultado_kelvin = celsius + 273.15
    print(f'Em celsius: {celsius}, fahrenheit: {resultado_fah}, kelvin: {resultado_kelvin}')
temperatura()
