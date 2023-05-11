import sys

interable = ['Eu', 'tenho', '__iter__']
iterator = interable.__iter__()
#ou
iterator = iter(interable)

print(next(iterator))
print(next(iterator))
print(next(iterator))

#GENERATOR EXPRESSION
#todo generator é um iterator
lista = [numero for numero in range(100)]
generator = (numero for numero in range(10)) 
#usado para dar o valor um por um
#o generator nao tem indice, tamanho

print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

print(next(generator))
print(next(generator))
print(next(generator))

#Introdução do generator functions

def generator(n=0):
    return 1

gen = generator( )