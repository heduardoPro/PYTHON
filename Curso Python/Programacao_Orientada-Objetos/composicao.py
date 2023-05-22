class Cliente:

    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

class Endereco:

    def __init__(self, rua, nummero) -> None:
        self.rua = rua
        self.numero = nummero


    def __del__(self):
        print('APAGANDO,', self.rua, self.numero) 

c1 = Cliente('Henrique')
c1.inserir_enderecos('Rua Antonio Noberto', 9)
c1.inserir_enderecos('Rua Antonio ', 10)
c1.inserir_enderecos('Rua Antonio brejo', 11)
c1.lista_endereco()