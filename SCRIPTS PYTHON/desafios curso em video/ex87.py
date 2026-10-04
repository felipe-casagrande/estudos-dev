matriz = [[0,0,0], [0,0,0],[0,0,0]]
par = 0
soma_coluna = 0
maior_segunda_linha = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite o valor da posição [{linha},{coluna}]: '))
print('-='*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end=' ')
        if matriz[linha][coluna] % 2 == 0:
            par+= matriz[linha][coluna] 
    print()
print(f'A soma de todos os pares é: {par}')

for linha in range(0,3):
    soma_coluna += matriz[linha][2]
print(f'A soma da terceira coluna é: {soma_coluna}')    
for coluna in range(0,3):
   if coluna == 0:
       maior_segunda_linha = matriz[1][coluna]
   elif matriz [1][coluna]> maior_segunda_linha:
       maior_segunda_linha = matriz[1][coluna]
print(f'O maior da segunda linha é {maior_segunda_linha}')
    
    