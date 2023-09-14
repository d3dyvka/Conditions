import math
a = int(input())
b = int(input())
c = int(input())
D = 0
x = 0

if b ** 2 - 4 * a * c == 0:
    D = b ** 2 - 4 * a * c
    print("У уравнения 1 корень:",-b / (2 * a))
elif b ** 2 - 4 * a * c > 0:
    D = b ** 2 - 4 * a * c
    x_1 = (-b + math.sqrt(D) )/ (2 * a)
    x_2 = (-b - math.sqrt(D)) / (2 * a) 
    if x_1 == x_2:
        print("У уравнения 1 корень:", x_1)
    else:
        print("У уравнения 2 корня\n", "x_1 =",round(x_1, 4), "\n", "x_2 =", round(x_2, 4))
elif b ** 2 - 4 * a * c < 0:
    print("корней нет")


