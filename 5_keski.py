leiviska = 8512
clavo = 425.6
bala = 13.3

bullets = float(input("Anna leiviskät.\n"))
naula = float(input("Anna naula.\n"))
luoti = float(input("Anna luodit.\n"))

a = bullets * leiviska
b = naula * clavo
c = bala * luoti

gramos = a + b + c
kilos = gramos / 1000
gramos_decimal = gramos - int(kilos) * 1000

print(f"Massa nykymittojen mukaan:\n{int(kilos)} kilogrammaa ja {gramos_decimal:.2f} grammaa.")