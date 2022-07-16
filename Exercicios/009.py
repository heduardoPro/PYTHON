### Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre em Dólares ela pode comprar
cash =float(input("Quanto de dinheiro você tem na carteira? "))
dolar = cash / 5.41
print("Com R${} você pode comprar US${:.2f}".format(cash, dolar))