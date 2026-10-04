def calcula_imposto_renda(salario):
    if salario<= 2112.00:
        imposto = 0.0
        return imposto
       
    elif salario <=2826.65:
        aliquota = 0.075
        deducao = 158.4
        imposto = salario*aliquota - deducao
        return imposto 
    elif salario <=3751.05:
        deducao = 370.4
        aliquota = 0.15
        imposto = salario*aliquota - deducao
        return imposto 
       
    elif salario <=4664.68:
        deducao = 651.73
        aliquota = 0.225
        imposto = salario*aliquota - deducao
        return imposto 
    elif salario >4664.68:
        deducao =884.96
        aliquota = 0.2750
        imposto = salario*aliquota - deducao
        return imposto 


def menu():
    print('Digite 1 para calcular imposto')
    print('Digite 2 para encerrar o programa')
    while True:
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            salario = float(input('Digite seu salário e te direi seus impostos: '))
            imposto = calcula_imposto_renda(salario)
            salario_liquido = salario - imposto
            if imposto == 0:
                print(f'Isento de taxas, salário de {salario:.2f}')
            else:
    
                print(f'Os impostos devidos é de {imposto:.2f}')
                print(f'O salario liquido é de {salario_liquido:.2f}')
        elif opcao == 2:
            print('Saindo...')
            break
menu()