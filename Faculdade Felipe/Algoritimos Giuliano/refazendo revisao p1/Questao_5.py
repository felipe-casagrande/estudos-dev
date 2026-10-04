def calcular_impostos_inss(salario_bruto):
    if salario_bruto<=1500.00:
        taxa = salario_bruto*0.075
        
    elif salario_bruto <=3000.00:
        taxa = salario_bruto*0.09
        
    elif salario_bruto >3000.00:
        taxa = salario_bruto*0.12

    inss = salario_bruto - taxa
    print(f'Salario de R${salario_bruto:.2f} foi descontado R${taxa:.2f} passou a ser R${inss:.2f}')
    return inss    


def calcular_irpf(inss):
    if inss <= 1500.00:
        print(f'Isento de taxas, salário se mantem em R${inss:.2f}')
        return inss
    elif inss<=4000:
        taxa = inss*0.075
        
    elif inss >4000.00:
        taxa = inss*0.15
        
    liquido = inss - taxa
    print(f'O salário após os descontos do inss foi para R${inss}, diminuindo ao IRPF no valor de R${taxa}, passou a ser R${liquido}')

    return liquido

def menu():
    print('Digite 1 para calcular impostos!')
    print('Digite 2 para encerrar o programa')
    while True:
        opcao = int(input('escolha uma opçao: '))
        if opcao == 1:
            salario_bruto = float(input('Digite o seu salário: '))
            resultado = calcular_impostos_inss(salario_bruto)
            final = (calcular_irpf(resultado))
        elif opcao == 2:
            print('encerrando..')
            break
menu()