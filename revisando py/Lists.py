#list[]
list = ['Eduardo', 'Laranja', 'Objetos', 'Avião'] #create list
numbers = [123, 568, 31, 999, 564]

print(list)
print(list[2])

#ordenação 
list.sort() #lista ordenada
print(list)
list.append('love')
list.sort(reverse=True) #Lista reversa
print(list)

test = ['a', 2]
print(test)
del test

print(min(numbers))
numbers.reverse()
print(numbers)
print(max(numbers))
print(sum(numbers))
print(len(numbers))

#extend list
list.extend(numbers)
print(list)

numbers.clear()
print(numbers)

phones = []
for number in range(0, 3):
    number = input('Enter numbers of Phone: ')
    phones.append(number) #Função para adicionar algo a uma lista

print(phones)

