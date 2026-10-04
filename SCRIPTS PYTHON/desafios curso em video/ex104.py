#jeito do felipao
'''
def leia_int():
    while True:
        n = input('digite um numero: ')
        if n.isnumeric() == True:
            break
        else:
            print('Erro')
    print(f'Você acabou de digitar o numero {n}') 


    
leia_int()
'''


#jeito do guanabara





def leia_int(msg):
    while True:
        ok = False
        valor = 0
        n = str(input(msg))
        if n.isnumeric() == True:
            valor = int(n)
            ok = True
        else:
            print('Erro')
            
        if ok == True:
            break
    return valor    



#progama principal
n = leia_int('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')