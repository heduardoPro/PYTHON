
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Joao', 20)
p2 = Pessoa('Maria', 35)
del p1.nome
print(p1.idade)
print(p1.__dict__)
print(vars(p2))
p1.__dict__['outra'] = 'coisa'
print(p1.__dict__)