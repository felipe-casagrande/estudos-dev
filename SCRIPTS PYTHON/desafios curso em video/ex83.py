expr = input('Digite a expressao: ')
lista = []
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Sua expressao esta correta!') 
else:
    print('Sua expressao esta incorreta!')           