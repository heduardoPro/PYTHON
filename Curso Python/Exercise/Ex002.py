cpf = '74682489070'
nove_digitos = cpf[:9]

indice = 10
soma = 0
for numero in nove_digitos:
    soma += int(numero) * indice
    indice -= 1

digito_1 = digito_1 if digito_1 <= 9 else 9
digito_1 = (soma * 10) % 11
print(digito_1)

