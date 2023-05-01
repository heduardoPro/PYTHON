lista = ['a', 1, 22, True, (0, 20), {'nome': 'Henrique'}]

for item in lista:
    if isinstance(item, str):
        print('STR')
        print(item, isinstance(item, str)) #verifica se tem a instancia na lista

    if isinstance(item, set):
        print('SET')
        print(item, isinstance(item, set))