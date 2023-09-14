a = int(input())
b = int(input())

if a % b == 0:
    print("Число", a,"кратно", b)
else:
    print("Число", a,"не кратно", b,"\n", "Остаток от деления =", a % b)