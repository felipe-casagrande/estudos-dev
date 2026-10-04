class Livro:
    def __init__(self,titulo:str,autor:str,ano:int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f'Livro: {self.titulo}\nAutor: {self.autor}\nAno:{self.ano}'

    def resumo(self):
        print(f'O livro {self.titulo} foi escrito pelo autor {self.autor} em {self.ano}')    

class Biblioteca:
    def __init__(self,nome:str,endereco:str):
        self.nome = nome
        self.endereco = endereco
        self.livros:Livro = []
        self.livros_emprestados = []
        self.usuario_pegaram_livro = []

    def adicionar_livro(self,livro:'Livro'):
        if livro not in self.livros:
            self.livros.append(livro)
            print(f'Livro {livro.titulo} adicionada a biblioteca')
        else:
            print('Esse livro já esta na biblioteca')


    def emprestar(self,usuario:'Usuario',livro):
        if livro in self.livros:
            self.livros_emprestados.append(livro)
            self.livros.remove(livro)  #removendo livro da biblioteca
            usuario.livros_usuario.append(livro)
            print(f'Emprestando livro para {usuario.nome}')

            if usuario not in self.usuario_pegaram_livro:
                self.usuario_pegaram_livro.append(usuario)
        else:
            print('Livro não disponivel no catalago')
             
           
    def listar_emprestimos(self):
        print('-'*30)
        print('LIVROS EMPRESTADOS')
        for livro in self.livros_emprestados:
            print(f'Titulo: {livro.titulo}')     

    def pegaram_livro(self):
        print('-'*30)
        print('Lista de Usuarios que pegaram livros: ')
        for user in self.usuario_pegaram_livro:
            print(f'Usuario: {user.nome}')

    def livros_disponiveis(self):
        print('-'*30)
        print('Livros disponiveis')
        for livro in self.livros:
            print(f'Livro: {livro.titulo}')

    def usuario_especifico(self,usuario:'Usuario'):
        print('-'*30)
        print(f'LIVROS DO {usuario.nome}')

        for c in usuario.livros_usuario:
            print(c)
            print('-'*30)

            

class Usuario:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_usuario:'Livro' = []                

    def listar_livros(self):
        print('-'*30)
        print(f'LIVROS DO {self.nome}')
        for livro in self.livros_usuario:
            print(f'Livro: {livro.titulo}')

    def pegar_livro(self,livro:Livro,biblioteca:'Biblioteca'):
        if livro not in self.livros_usuario and livro in biblioteca.livros:
            return biblioteca.emprestar(self,livro)
        
        else:
            print(f'O usuario {self.nome} ja tem esse livro ou nao tem na biblioteca')        






livro1 = Livro('Prova','felipe',2025)
livro2 = Livro('Naruto','PL',2025)
livro3 = Livro('Avatar','vitao',2025)
livro4 = Livro('Atack on titan', 'igor',2024)

User1 = Usuario('felipe','20221321')
User2 = Usuario('Pl','2022221')

b1 = Biblioteca('Vassouras','Saquarema')   

#-------------------------------------comandos------------------
#Adicionando os livros criados a biblioteca
b1.adicionar_livro(livro1)
b1.adicionar_livro(livro2)
b1.adicionar_livro(livro3)
b1.adicionar_livro(livro4)

#Fazendo o usuario pegar um livro passando o livro e a biblioteca, onde nessa funçao ira puxar o metedo emprestar da biblioteca.
#Assim adicionando o livro pro usuario, colocando o livro na lista de emprestados, tirando o livro da lista de disponiveis.
User1.pegar_livro(livro1,b1)
User2.pegar_livro(livro2,b1)
User1.pegar_livro(livro3,b1)

#Mostrando os livros que foram pegos da biblioteca
b1.listar_emprestimos()

#mostrando os usuarios que pegaram livros
b1.pegaram_livro()

#mostrando livros disponiveis
b1.livros_disponiveis()

#mostrando livros que o usuario pegou atraves da biblioteca
b1.usuario_especifico(User1)
b1.usuario_especifico(User2)
