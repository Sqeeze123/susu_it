import math

first_x = float(input("Введите x0: "))
y0 = float(input("Введите y0: "))
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))


distance = math.sqrt((x1 - first_x)**2 + (y1 - y0)**2)
print(f"Расстояние ({first_x}, {y0}) и ({x1}, {y1}): {distance}")
