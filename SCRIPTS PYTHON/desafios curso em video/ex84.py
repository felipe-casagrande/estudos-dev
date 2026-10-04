pessoas = list()
geral = list()
maior = menor = 0
while True:
    geral.append(input('Digite seu nome: '))
    geral.append(float(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        maior=menor= geral[1]
    else:
        if geral[1] > maior:
            maior = geral[1]
        if geral[1] < menor:
            menor = geral[1]
    pessoas.append(geral[:])        
    geral.clear()
    seguir = input('Deseja seguir [sim/nao]? ')
    if seguir == 'nao':
        break       
print(f'O maior peso é: {maior}. Peso de ', end='' )
#print(f'O numero de cadastrados foram {len(pessoas)}')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso é: {menor}, Peso do' ,end='')
for c in pessoas:
    if c[1] == menor:
        print(f'[{c[0]}]', end='')      
    