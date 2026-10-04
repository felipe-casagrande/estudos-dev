def busca_sequencial(livros,id_alvo):
    for livro in livros:
        if livro['id'] == id_alvo:
            return livro
    return - 1


livros = [
{"id": 105, "titulo": "O Senhor dos Anéis"}, 
{"id": 210, "titulo": "1984"}, 
{"id": 157, "titulo": "Dom Casmurro"}, 
{"id": 332, "titulo": "O Pequeno Príncipe"}, 
{"id": 190, "titulo": "Harry Potter"},
]  
id_alvo = int(input('Digite o id do livro desejado:'))
busca = busca_sequencial(livros,id_alvo)
if busca != -1:
    print(f'O livro {busca['titulo']} foi encontrado')
else:
    print('Nao encontrado')