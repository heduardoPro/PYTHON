# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:

    def __init__(self, marca) -> None:
        self.marca = marca
        self._motor = None
        self._fabricante= None

    @property
    def motor(self):
         return self._motor
    
    @motor.setter
    def motor(self, other):
         self._motor = other
    
    @property
    def fabricante(self):
         return self._fabricante
    
    @fabricante.setter
    def fabricante(self, other):
         self._fabricante = other

class Motor:

    def __init__(self, nome) -> None:
        self.nome = nome

class Fabricante:

    def __init__(self, nome) -> None:
         self.nome = nome

ferrari = Carro('Ferrari')
fabricante = Fabricante('f1')
motor_1_0 = Motor('1.0')
ferrari.fabricante = fabricante
ferrari.motor = motor_1_0
print(ferrari.marca, ferrari.fabricante.nome, ferrari.motor.nome)