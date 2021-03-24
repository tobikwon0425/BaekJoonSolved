a = int(input())
b = int(input())
c = int(input())

mul = a * b * c
list_mul = str(mul)
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for num in range(10):
    for i in list_mul:
        if i == str(num):
            count[num] += 1
    print(count[num])
