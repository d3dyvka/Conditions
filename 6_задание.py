import math
x = float(input())
y = float(input())
R = float(input())

hyp = math.sqrt(x ** 2 + y ** 2)

if hyp <= R:
    print("Принадлежит")
else:
    print("не принадлежит")