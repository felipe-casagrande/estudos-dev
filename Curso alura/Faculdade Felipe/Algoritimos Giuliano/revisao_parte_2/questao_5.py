'''Tarefa 5 – Calculadora de Descontos Progressivos
Uma loja oferece descontos progressivos conforme o valor da compra:
• Até R$ 100 → 5%
• De R$ 100,01 a R$ 500 → 10%
• Acima de R$ 500 → 15%
O sistema deve receber o valor da compra e calcular o valor final com desconto aplicado.'''
def calculadora(valor):
    if valor <= 100:
        total = valor - (valor*0.05)
        print(f'O valor total com 5% de desconto é de R${total}')
    elif valor >=100.01 and valor <=500:
        total = valor - (valor*0.10)
        print(f'O valor total com 10% de desconto é de R${total}')
    elif valor>500:
        total = valor - (valor*0.15)
        print(f'O valor total com 15% de desconto é de R${total}')


def menu():
    print('Digite 1 para calcular o desconto: ')
    print('Digite 2 para sair do programa')
    while True:
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            valor = float(input('Digite o valor da compra: '))
            calculadora(valor)
        elif opcao == 2:
            print('saindo..')
            break
menu()
