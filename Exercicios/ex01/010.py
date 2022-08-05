larg = float(input("Largura da parede: "))
alt = float(input("Alturra da parede: "))
área = larg * alt
print("As suas dimensões da sua parede são {}x{} e sua área é de {}m²".format(larg, alt, área))
tinta = área / 2
print("Para pintar essa parede você percisara de {}l de tinta".format(tinta))