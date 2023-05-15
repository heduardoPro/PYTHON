class Pessoa:
    
    def __init__(self, nome, sobrenome) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome

    def __str__(self) -> str:
        return f'Nome: {self.__nome} \nSobrenome: {self.__sobrenome}'
    
pessoa = Pessoa('Henrique', 'Eduardo')
print(pessoa)