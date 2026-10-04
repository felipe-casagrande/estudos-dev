def classificacao(leves,graves,gravissimas):
    if leves == 0  and graves == 0 and gravissimas == 0:
        return 'Motorista excelente'
    elif leves <=2 and graves == 0 and gravissimas == 0:
        return 'Motorista bom'
    elif leves <=4 and graves ==0 and gravissimas == 0:
        return 'Motorista regular'
    elif graves == 1 and gravissimas == 0:
        return 'Motorista regular'
    elif (leves >4 or graves <=2) and gravissimas == 0:
        return 'Motorista ruim'
    elif graves>2 or gravissimas>0:
        return 'Motorista perigoso'
    else:
        return 'classificaçãi indefinida'
    

def menu():
    print('Digite 1 para inicar o programa')
    print('Digite 2 para encerrar')
    while True:
        opcao = int(input('escolha uma opçao: '))
        if opcao == 1:
            leves = int(input('Digite a quantidade de multas leves: '))
            graves = int(input('Digite a quantidade de multas graves: '))
            gravissimas = int(input('Digite a quantidade de multas gravissimas: '))
            resultado = classificacao(leves,graves,gravissimas)
            print(resultado)
                         
menu()        