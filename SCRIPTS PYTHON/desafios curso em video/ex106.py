def ajuda(resp):
    while True:
        p = str(input(resp))
        if p == 'Fim':
            break
        
        else:
            mensagem = help(p)
    return mensagem        


função = ajuda('Digite uma função ou uma biblioteca: ')
