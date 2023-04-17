#criando função 
def sum():
    print('Enter two numbers inters: ')
    x = int(input('>>> '))
    y = int(input('>>> '))

    print('Sum: ', x + y)
#Função com paramentros
def greeting(name, age):
    print('Hello ' + name + ', you are ' + age + '!')


#Chamando a função
sum()
greeting('Henrique', '20')