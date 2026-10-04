


def notas(*num, sit=0):
    """ """
    lista = list()
    for c in num:
        lista.append(c)
    dicionario['Quantidade'] = len(lista) 
    media = sum(lista) / len(lista) 
    dicionario['Media'] = media
    dicionario['Maxima'] = max(lista)
    dicionario['Menor'] = min(lista)
    if sit == True:
        if dicionario['Media'] < 7 and dicionario['Media'] >5:
            dicionario['Situação'] = 'Razoavel!'    
        elif dicionario['Media'] > 7:
            dicionario['Situação'] = 'Boa!'
        else:
            dicionario['Situação'] = 'Ruim!'
    print(lista)
    return dicionario



dicionario = dict()
resp = notas(5.5, 10,5,10,6, sit=True)
print(resp)   