lista_final = list()
while True: 
    aluno = input('Digite seu nome: ')
    p1 = float(input('Digite a nota da p1: '))
    p2 = float(input('Digite a nota da p2: '))
    media = (p1+p2)/2
    seguir = input('Deseja ver mais alunos?  [sim/nao]')
    lista_final.append([aluno,[p1,p2],media])
    if seguir == 'nao':
        break    

print(f'{'No.':<4}.{'NOME':<10}{'MEDIA':>8}')  #deixando organizado a tabela
print('-='*30)

for i, nomes in enumerate(lista_final):                     #i seria o indice e nomes seria toda a lista final percorrida, o enumerate #vai servir para dar indice e mostrar os itens que foram percorridos   , o nomes 'vira' a lista final nesse laço                                  
    print(f'{i:<4}{nomes[0]:<10}media {nomes[2]:>8}')    
while True:
        ver_notas = int(input('Deseja ver as notas de qual aluno?   [999 interrompe]'))
        if ver_notas == 999:
            break
        if ver_notas <= len(nomes)-1: 
            print(f'As notas do {lista_final[ver_notas][0]}, as notas sao {lista_final[ver_notas][1]}')
    
                                                    #o ver notas é a resposta, o digito dele tem q ser igual a algum indice ja mostrando no enumerate
                                                    #colocando lista_final[ver_notas][0], eu estou dizendo, no indice igual ver notas, mostre o primeiro item da lista, que seria o nome
