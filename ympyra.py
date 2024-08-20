import math

pi = math.pi
circulo = int(input("Kirjoita ympyrän säde (cm): "))
area = (circulo*circulo) * pi

print(f"Ympyrän pinta-ala on: {"%.2f" %area} cm^2")