###Seno, Cosseno e Tangente
import math
ang = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(ang))
print("O ângulo de {:.0f}° tem o SENO de {:.2f} ".format(ang, seno))
cos = math.cos(math.radians(ang))
print("O ângulo de {:.0f}° tem o COSSENO de {:.2f} ".format(ang, cos))
tang = math.tan(math.radians(ang))
print("O ângulo de {:.0f}° tem a TANGENTE de {:.2f} ".format(ang, tang))