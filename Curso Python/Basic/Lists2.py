lista = [10, 20, 30, 40]
print(lista)
lista[2] = 60
#deletar item da lista
del lista[3]
print(lista)

#adicionando item a lista
lista.append(50)
print(lista)

ultimo_valor = lista.pop() #remove o ultimo elemento da lista ou utlizando o indice especifico
lista.append(75)
print(lista)    

lista2 = [12, 45, 50, 'henrique', 10] 
del lista2[-1] #deleta o ultimo item da lista
print(lista2)

#limpar a lista
lista2.clear()
print('lista 2 foi limpa', lista2)

#insert
lista.insert(2, 5) #troca elemento no indcie escolhido
print(lista)

#União de listas
listaA = [1, 2, 3]
listaB = [4, 5, 6]
listaC = listaA + listaB
print(listaC)
listaA.extend(listaB) 
print(listaA)

listaA = listaB.copy()
print(listaA)