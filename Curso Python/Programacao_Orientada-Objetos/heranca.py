class Pessoa:

    def __init__(self, nome) -> None:
        self.nome = nome

    def falar_nome_classe(self):
        print(self.nome ,self.__class__.__name__)

class Cliente(Pessoa):
    ...
class Aluno(Pessoa):
    ...


p1 = Pessoa('Pessoa')
p1.falar_nome_classe()
c1 = Cliente('Henrique')
c1.falar_nome_classe()
a1 = Aluno('Maria')
a1.falar_nome_classe()