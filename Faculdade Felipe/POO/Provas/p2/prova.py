class Imovel:
    def __init__(self,endereco:str,metragem:int,valor:float):
        self.endereco = endereco
        self.metragem = metragem
        self.valor = valor

    def exibir_info(self):
        print('Informações do imovel...')
        print(f'Endereço: {self.endereco}\nMetragem: {self.metragem} metros\nValor: R${self.valor}')   

    def tipo_imovel(self):
        return None

class Casa(Imovel):
    def __init__(self, endereco, metragem, valor,num_quartos:int):
        super().__init__(endereco, metragem, valor)
        self.num_quartos = num_quartos

    def tipo_imovel(self):
        print('Tipo do Imovel: Casa')

    def exibir_info(self):
        print('Informações da casa..')
        print(f'Endereço: {self.endereco}\nMetragem: {self.metragem} metros\nValor: R${self.valor}\nNumero de quartos: {self.num_quartos}') 

class Apartamento(Imovel):
    def __init__(self, endereco, metragem, valor,andar:int):
        super().__init__(endereco, metragem, valor)
        self.andar = andar

    def tipo_imovel(self):
        print('Tipo do Imovel: Apartamento')     

    def exibir_info(self):
        print('Informações do apartamento..')
        print(f'Endereço: {self.endereco}\nMetragem: {self.metragem} metros\nValor: R${self.valor}\nQuantidade de andares: {self.andar}') 
 

def mostrar_tipo(imovel:Imovel):
    imovel.tipo_imovel()



# instancias
imovel1 = Imovel('Maracana',2000,100000)
casa1 = Casa('Rua das Oliveiras',98,100000,2)
apartamento1 = Apartamento('Barra da Tijuca',500,100000,3)



#Funcoes

#Casa
casa1.exibir_info()
mostrar_tipo(casa1)

#Apartamento
print('')

apartamento1.exibir_info()
mostrar_tipo(apartamento1)


#Imovel sem ser casa e apartamento
print('')
imovel1.exibir_info()
print(mostrar_tipo(imovel1))