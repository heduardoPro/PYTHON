#CATETOS E HIPOTENUSA
import math
CO = float(input("Digite o comprimento do cateto oposto: "))
CA = float(input("Digite o comprimento do cateto adjacente: "))
hi = math.hypot(CO, CA)
print("A hipotenusa ira medir {:.2f}".format(hi))