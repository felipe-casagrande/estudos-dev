class Pessoa:
    def __init__(self,nome,sobrenome,idade,altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        self.vida =100
        self.vivo = True

    def falar(self,mensagem):
        print(f'{self.nome} : {mensagem}')

    def andar(self):
        print(f'{self.nome} esta se movendo ...')   

    def parar(self):
        print(f'{self.nome} parou')