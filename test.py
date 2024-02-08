#1
print("Задание 1")
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

#2
print("Задание 2")
import math

while True:
    n = input("Введите n: ")
    if n.isdigit()==False:
        print("Введите ещё раз ")
    else:
        break

max=0
for k in range(1, int(n)+1):
    if math.factorial(k) <= int(n):
        max = k
    else:
        break

k=max
if n==0:
    k=n
print(k)