import random
n = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
for numeros in n:
    print(f'{numeros}', end=' ')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteadi foi {min(n)}')    