def inverter_string(s):
    if s == '':
        return ''
    else:
        return inverter_string(s[1:])+ s[0]
    
string = input('Digite uma palavra e eu irei inverter: ')
resultado = (inverter_string(string))    
print(resultado)