import math

x0 = float(input("Введите x0: "))
y0 = float(input("Введите y0: "))
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))

distance = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
print(f"Расстояние между двумя точками ({x0}, {y0}) и ({x1}, {y1}): {distance}")
