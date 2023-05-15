class Carro:

    def __init__(self, marca, modelo, km, cor, placa, peso) -> None:
        self.marca = marca
        self.modelo = modelo
        self.km = km
        self.cor = cor
        self.placa = placa
        self.peso = peso

    def ligar(self):
        print(f'\nO carro {self.marca} ligou')
    
    def acelerar(self):
        print(f'\nO carro {self.marca} está acelerando...')

    def __str__(self) -> str:
        return 'Marca: {} \nModelo: {} \nKm rodados: {} \nCor: {} \nPlaca: {} \nPeso: {}'.format(self.marca, self.modelo, self.km, self.cor, self.placa, self.peso)

veiculo = Carro('FIAT', 'STRADA', 0.0, 'VERMELHO', 'HCK0FL23', 22.000)
print(veiculo)

veiculo.ligar()
veiculo.acelerar()