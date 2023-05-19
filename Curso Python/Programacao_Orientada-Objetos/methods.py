# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #Metodo da classe 
    def medodo_de_classe(cls):
         print('Hey')

    @classmethod 
    def criar_com_50_anos(cls, nome): #factories metodo de fábrica
         return cls(nome, 50)
    
    @classmethod 
    def cria_sem_nome(cls, idade):
         return cls('Anônima', idade)
    
p1 = Pessoa('Eu', 20)
p2 = Pessoa.criar_com_50_anos('Marta')
p3 = Pessoa.cria_sem_nome(25)
print(Pessoa.ano)
Pessoa.medodo_de_classe()
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)