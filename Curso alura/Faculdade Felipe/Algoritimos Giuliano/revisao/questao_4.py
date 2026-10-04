def imposto():
    categoria = input('Deseja calcular impostos de uma mercadoria ou de um serviço? ')
    while categoria != 'serviço' and categoria !='mercadoria':
        print('Categoria invalida, digite uma valida!')
        categoria = input('Deseja calcular impostos de uma mercadoria ou de um serviço? ')
    valor = float(input('Digite o valor do base: '))
    if categoria == 'mercadoria':
        icms = valor*0.18
        total = valor + icms
        print(total)
    elif categoria == 'serviço':
        iss = valor*0.05
        total = valor+iss
        print(total)
imposto()                