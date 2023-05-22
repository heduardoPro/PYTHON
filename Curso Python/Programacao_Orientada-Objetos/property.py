class Caneta:

    def __init__(self, cor) -> None:
        self.__cor = cor

    def get_cor(self):
        return self.__cor
    
    def set_cor(self, other):
        self.__cor = other

    def __str__(self) -> str:
        return f'A caneta tem a cor {self.get_cor()}'
    
caneta = Caneta('Preta')
print(caneta)
caneta.set_cor('Azul')
print(caneta)