def calcula_salario(salario):
    if salario <=2800:
        aumento = salario*0.20
        return aumento
       
    elif salario <=7000.00:
        aumento = salario*0.15
      
        return aumento
    elif salario <=15000.00:
        aumento = salario*0.1
        return aumento
    elif salario >15000.00:
        aumento = salario*0.05
        return aumento
    
def menu():
    print('Digite 1 para calcular o aumento do salário!')
    print('Digite 2 para encerrar o programa')
    while True:
        opcao = int(input('Digite uma opção:' ))
        if opcao == 1:
            salario_base = float(input('Digite seu salario base: '))
            aumento = (calcula_salario(salario_base))
            salario_aumentado = salario_base + aumento
            print(f'O salário de {salario_base:.2f}, com um aumento de {aumento:.2f} foi para {salario_aumentado}')
        elif opcao == 2:
            print('saindo...')
            break

menu()