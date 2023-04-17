#definindo funções
def printar():
    print('Esta função ira imprimir esse campo de texto')


def saudacao(nome='Sem nome'):
    print('Bem vindo', nome)

#funções com paramentros(argumentos)
def paramentros(a, b, c):
    print((a + b) * c)

def soma(x, y, z):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

#chamando função
saudacao()
printar()
paramentros(1, 2, 2)
#argumentos nomeados
paramentros(b=1, c=2, a=10)
soma(7, 9, 0)
soma(y=9, z=0, x=7)
