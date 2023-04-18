# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicar(numero, x):
    return numero * x

num = int(input('Digite um número: '))
for multiplicador in range(2, 5):
    var = multiplicar(num, multiplicador) 
    print(var, end='-')