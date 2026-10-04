def busca_binaria(livros,id_alvo):
    inicio, fim = 0, len(livros) -1
    livros.sort(key= lambda livro: livro['id'])
    while inicio <= fim:
        meio = (inicio + fim ) // 2
        if livros[meio]['id'] == id_alvo:
            return livros[meio]
        elif livros[meio]['id'] < id_alvo:
            inicio = meio + 1
        else:
            fim = meio -1
    return -1        


livros = [
{"id": 105, "titulo": "O Senhor dos Anéis"}, 
{"id": 210, "titulo": "1984"}, 
{"id": 157, "titulo": "Dom Casmurro"}, 
{"id": 332, "titulo": "O Pequeno Príncipe"}, 
{"id": 190, "titulo": "Harry Potter"},
]      
id_alvo = int(input('Digite o id do livro: '))
busca = busca_binaria(livros, id_alvo)
if busca != -1:
    print(f'O livro {busca['titulo']} foi encontrado!')
else:
    print('Id nao encontrado')