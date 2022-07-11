###Tipos de print

print('Oi' + 'Olá')
print('oi'*5)# Ira printar 5 vezes a palavra "Oi"
print('='*20)

nome = input('Qual seu nome? ')
print('Prazer{:=^20}'.format(nome))

n1=int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2
print("A soma e {}, a divisão e {}, a multiplicação e {},".format(s, d, m), end=' ')
print("a divisão inteira e {} a potencia e {} ".format(di, e))