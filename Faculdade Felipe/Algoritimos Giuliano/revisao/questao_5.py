def salario():
    salario_bruto = float(input('Digite seu salário: '))
    if salario_bruto <= 1500.00:
        inss = salario_bruto - (salario_bruto*0.075)
        print(inss)
    elif salario_bruto>1500.00 and salario_bruto <= 3000.00:
        inss= salario_bruto - (salario_bruto*0.09)
        print(inss)    
    else:
        inss = salario_bruto - (salario_bruto*0.12)
        print(inss)

    # agora vamos para o irpf
    
    if inss <= 2000.00:
        print('isento de irpf')
    elif inss > 2000.00 and inss <= 4000.00:
        liquido = inss -(inss*0.075)
        print(liquido)
    else:
        liquido = inss - (inss*0.15)
        print(liquido)
        