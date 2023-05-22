class Carro:

    def __init__(self, cor) -> None:
        #private
        self.__cor = cor

    #getter
    @property
    def cor(self): #obter valor        
        return self.__cor
    #setter
    @cor.setter
    def cor(self, other): #alterar valor        
        self.__cor = other
    
    def __str__(self):
        return f'Cor: {self.__cor}'
    
veiculo = Carro('Roxo')
print(veiculo.get_cor)
print(veiculo.cor)