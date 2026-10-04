def calcula_bonificacao(taxa_bonus,salario_base):
    bonus = salario_base + (salario_base*taxa_bonus)
    print(f'O salario de {salario_base} com um adicional de {taxa_bonus*100}% de bônus da: {bonus}')

def menu():
    print('Digite 1 para calcularmos o seu bônus!')
    print('Digite 2 para sair do programa.')    
    while True:
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            salario_base = float(input('Digite o valor do seu sálario base: '))
            taxa_bonus = float(input('Digite o valor da sua taxa de bonus em porcentagem'))
            taxa_bonus = taxa_bonus/100
            calcula_bonificacao(taxa_bonus,salario_base)
        else:
            print('saindo...')
            break
            

menu()