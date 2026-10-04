import random
from time import sleep
print('-='*30)
print('         JOGA NA MEGA SENA           ')
print('-='*30)
quantidade_sorteios = int(input('Quantos jogos serão sorteados? '))

jogos_realizados = 1
lista_reset = list()
lista_final = list()
print(f'Sorteando {quantidade_sorteios} jogos...')
print('-='*30)

while jogos_realizados <= quantidade_sorteios:
    quantidade_numeros_para_o_sorteios = 0
    while True:
        numero = random.randint(1,60)
        if numero not in lista_reset:
            lista_reset.append(numero)
            quantidade_numeros_para_o_sorteios+=1
        if quantidade_numeros_para_o_sorteios >= 6:
            break
    lista_final.append(lista_reset[:])
    lista_reset.clear()
    jogos_realizados+=1

for indice, lista in enumerate(lista_final):
    print(f'Para o jogo {indice+1}°, use os numeros: {lista_final[indice]}')
    sleep(1)
print('-='*3, 'BOA SORTE', '-='*3)