def multiplicador(*args):
    total = 1
    for x in args:
        total *= x
    return total


def par_impar():
    x = int(input('Digite um numero qualquer: '))
    if x % 2 == 0:
        return '{} é par.'.format(x)
    return '{} é impar.'.format(x)

var = multiplicador(1, 1, 1)
print(var)
var_2 = par_impar()
print(var_2)