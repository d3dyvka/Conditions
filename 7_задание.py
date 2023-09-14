import math
print("Выберите фигуру: Прямоугольник - 1, Треугольник - 2, Круг - 3")
typ = input()
if typ == "1":
    print("Введите значение 2х сторон прямоугольника")
    a = int(input())
    b = int(input())
    print("S =", a * b)
elif typ == "2":
    print("Введите значение высоты и основания треугольника")
    h = int(input())
    osn = int(input())
    print("S =", 1 / 2 * osn * h)
elif typ == "3":
    print("Введите значение радиуса круга")
    R = int(input())
    print("S =", 2 * math.pi * R)
else:
    print("Такой команды нет")