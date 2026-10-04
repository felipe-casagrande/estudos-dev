numero = int(input('Digite um numero e eu te direi se ele é perfeito!'))
soma = []
for c in range(numero):
    if numero%(c+1)==0:
        soma.append(c+1)
        print(soma)
soma.remove(soma[-1])        
print(soma)
total = sum(soma)
if total == numero:
    print(f'{numero} é um numero perfeito!')