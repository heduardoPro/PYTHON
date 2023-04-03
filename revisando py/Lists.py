list = ['Eduardo', 'Laranja', 'Objetos', 'Avião'] #create list

print(list)
print(list[2])

#ordenação 
list.sort() #lista ordenada
print(list)
list.sort(reverse=True) #Lista reversa
print(list)

phones = []
for number in range(0, 3):
    number = input('Enter numbers of Phone: ')
    phones.append(number) #Função para adicionar algo a uma lista

print(phones)
