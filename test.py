s=0

while True:
    k = input("Введите k: ")
    if k.isdigit()==False:
        print("Введите ещё раз ")
    else:
        break

while True:
    m = input("Введите m: ")
    if m.isdigit() == False:
        print("Введите ещё раз ")
    else:
        break

for i in range(int(k), int(m) + 1):
    if i < int(m) + 1:
        s += i ** 2
print(s)