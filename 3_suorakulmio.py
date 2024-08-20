largo_rectangulo = int(input("Kirjoita suorakulmion kanta (cm): "))
ancho_rectangulo = int(input("Kirjoita suorakulmion korkeus (cm): "))
perimetro = (largo_rectangulo * 2) + (ancho_rectangulo * 2)
area = largo_rectangulo * ancho_rectangulo
print(f"Suorakulmion pinta-ala on: {area} cm^2 \nSuorakulmion piiren on {perimetro} cm")
