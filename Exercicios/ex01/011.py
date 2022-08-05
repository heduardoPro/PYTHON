from ctypes.wintypes import PINT


preço = float(input("Qual o preço do produto? R$"))
np = preço - (preço * 5 / 100)
print("O produto que custava {}, na promoção com desconto de 5% vai custar {}".format(preço, np))