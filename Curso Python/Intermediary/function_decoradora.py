def decoradora(funcao):
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = funcao(*args, **kwargs)
        return res
    return aninhada

@decoradora
def funcao_com_decoradora(x, y):
    return x + y
soma = funcao_com_decoradora(5,5)
print(soma)