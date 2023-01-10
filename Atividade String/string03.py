import re

line1 = input()
line2 = input()
cpf = ""
soma = ""
decimal = ""
numeros = re.findall('\d|\.', line1)
print(numeros)
max = 11
for i in range(max):
    if(i != "."):
        cpf = cpf + numeros[i]
    else:
        max += 1

for i in range(max+1, 17):
    if(numeros[i] == "."):
        soma = int(soma)
        cont = 0
        for j in range(i+1, 17):
            decimal = decimal + numeros[j]
            cont += 1
            if(cont > 2):
                break
        #decimal = int(decimal)
        #decimal = decimal/100
        soma = soma + decimal
        break
    soma = soma + numeros[i]
soma = float(soma)

print('CPF: ', cpf)
print('SOMA: ', soma)