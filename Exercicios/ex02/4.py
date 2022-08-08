#Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do novo salário reajustado de acordo com a tabela abaixo:
salario = float(input('Enter current salary:'))

if(salario < 500):
    novo = salario + (salario * 0.15)
    print('The new salary:', novo)
if((salario >= 500) and (salario <= 1000)):
    novo = salario + (salario * 0.10)
    print('The new salary is: ', novo)
if(salario > 1000):
    novo = salario + (salario * 0.05)
    print('The new salary is: ', novo)