def calculadora(valor):
    if valor <=100:
        desconto = valor*0.05
        
    elif valor <= 500:
        desconto = valor*0.10
    elif valor >500:
        desconto = valor*0.15

    return desconto 
def menu():

    while True:
        opcao = int(input('Digite a opção desejada: '))    
        if opcao == 1:
            valor = float(input('Digite o valor da compra: : '))
            desconto = calculadora(valor)
            total = valor -  desconto
            print(f'O valor era de R${valor:.2f}, com R${desconto:.2f} de desconto passou a ser {total}')
        elif opcao == 2:
            print('saindo...')
            break

menu()               