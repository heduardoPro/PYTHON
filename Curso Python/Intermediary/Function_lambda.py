lista = [
    {'nome': 'Maria', 'Sobrenome': 'Eduarda'},
    {'nome': 'Antony', 'Sobrenome': 'Yan'},
    {'nome': 'Kelly', 'Sobrenome': 'Vitoria'},
    {'nome': 'Pedro', 'Sobrenome': 'Lucas'},
]
'''
METODO NORMAL

def encontra(item):
    return item['nome']
lista.sort(key=encontra)
'''
#FUNÇÃO LAMBDA
lista.sort(key=lambda item: item['nome'])

for item in lista:
    print(item)
