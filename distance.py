import math

x0 = int(input("Введите x0: "))
y0 = int(input("Введите y0: "))
x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))

distance = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
print(distance)
