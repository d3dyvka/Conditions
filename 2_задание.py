a = int(input())
b = int(input())
c = int(input())

if a != b:
    if a != c:
        if b != c:
            print(int((a+b+c) / 3))
        else:
            print("Ошибка")
    else:
        print("Ошибка")
else:
    print("Ошибка")