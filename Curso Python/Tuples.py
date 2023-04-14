#introdução ao desempacotamento
#Tuplas - Tuples


#desempacotamento de listas
_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2, _) 

#Tuplas
nomes = ('Eduardo', 'João', 'Vitoria')
print(nomes)
#Uma tuple é imutavel, ou seja, não precisa mudor algum valor nela

#conversão de list para tuple
lista = [1, 2, 3]
print(lista)
lista_conver = tuple(lista) #pode converter ao contrario = list(xxxx)
print(lista_conver)