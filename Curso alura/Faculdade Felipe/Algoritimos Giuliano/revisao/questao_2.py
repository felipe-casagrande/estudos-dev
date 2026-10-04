
def classificação():
    
    excelente = []
    bom = []
    regular= []
    ruim = []
    perigoso = []
    while True:
        motorista = input('nome do motorista:')
        multas_leves = int(input(f'quantidade de multas leves do motorista {motorista}:'))
        multas_grave = int(input(f'quantidade de multas graves do motorista {motorista}:'))
        multas_gravissima = int(input(f'quantidade de multas gravissimas do motorista {motorista}:'))
        if multas_leves == 0 and multas_grave == 0 and multas_gravissima == 0:
            excelente.append(motorista)
            print(f'Motorista {motorista} foi adicionado a classe excelente')
        elif multas_leves <=2 and multas_grave == 0 and multas_gravissima == 0:
            bom.append(motorista)
            print(f'Motorista {motorista} foi adicionado a classe bom')
        elif multas_leves <= 4 and multas_grave == 1 and multas_gravissima == 0:
            regular.append(motorista)
            print(f'Motorista {motorista} foi adicionado a classe regular')
        elif multas_leves > 4 or (multas_grave <=2 and multas_gravissima == 0):
            ruim.append(motorista)   
            print(f'Motorista {motorista} foi adicionado a classe ruim')
        elif multas_grave > 2 or multas_gravissima >0:
            perigoso.append(motorista)
            print(f'Motorista {motorista} foi adicionado a classe perigoso')
        continuar = int(input('deseja adiocinar mais algum motorista?    1 = sim, 2 = nao: ' ))
        if continuar == 2:
            break
    print('Classificação final dos motoristas')  
    print('Excelente: ',','.join(excelente))   
    print('Bom: ',','.join(bom))
    print('Regular: ',','.join(regular))     
    print('Ruim: ',','.join(ruim))
    print('Perigoso: ',','.join(perigoso))
classificação()        
   