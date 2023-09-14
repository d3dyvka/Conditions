a = int(input())
if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                print("Високосный")
            elif a % 400 != 0:
                  print("Не високосный")
        elif a % 100 != 0:
              print("високосный")
else:
      print("не високосный")