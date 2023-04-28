# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
    'nome': 'Henrique Eduardo',
    'sobrenome': 'Azevedo',
    'idade': 20,
    'altura': 1.80,
}
print(len(d1))
print(d1.keys())
print(list(d1.values()))
#print(list(pessoa.items()))
for chave, valor in d1.items():
    print(chave, valor)
d1.setdefault('endereço', 'João Catingueira')
print(d1)

#d2 = d1.copy() // cópia raza
d2 = copy.deepcopy(d1) # 

d2['sobrenome'] = 1000
print(d1)
print(d2)

p1 = {
    'nome': 'Henrique',
    'sobrenome': 'Eduardo',
}

nome = p1.pop('nome')
print(nome)
print(p1)

ultima_chave = p1.popitem() #pega a ultima chave do dicionario
print(ultima_chave)
print(p1)


p1.update(nome='Pedro', idade=20)
print(p1)