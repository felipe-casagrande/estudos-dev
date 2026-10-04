def calculo(valor,servico):
    if servico == 'mercadoria':
       imposto = valor*0.18
       return imposto
       
    elif servico == 'serviço':
        imposto = valor*0.05
        return imposto
def menu():
    print('Digite 1 para calcular os impostos')
    print('Digite 2 para fechar o programa')
    while True:
        opcao = int(input('escolha uma opçao: '))
        if opcao == 1:
            valor = float(input('Digite o valor: '))
            tributo = int(input('Digite 1 para mercadoria e digite 2 para serviços: '))
            if tributo == 1:
              tributo= 'mercadoria'
            elif tributo == 2:
                tributo = 'serviço'
            imposto= calculo(valor,tributo)
            total = valor - imposto
            print(f'O tributo escolhido foi {tributo}.O valor de impostos a ser pago é {imposto}, descontado do valor inicial de {valor}, o total liquido será de {total}')
            
        elif opcao == 2:
            print('saindo...')
            break    

menu()        