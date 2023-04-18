#introdução a Dicionarios ou classe dict()
pessoa = {
    'nome': 'Henrique Eduardo',
    'sobrenome': 'Azevedo',
    'idade': 20,
    'altura': 1.80,
    'endereço': [
        {'rua': 'Jose Ademar do Nascimento', 'número': 106},
        {'rua': 'Antonio Noberto', 'número': 00},
    ],
}

#print(pessoa, type(pessoa))
#O dicionario tem acessibilidade maior
print(pessoa['idade'])
print(pessoa['sobrenome'])

#Manipulando chaves e valores no dicionario

chave = 'nome'

pessoa[chave] = 'Maria Eduarda'
print(pessoa)

del pessoa['altura']
print(pessoa)
print(pessoa['altura'])