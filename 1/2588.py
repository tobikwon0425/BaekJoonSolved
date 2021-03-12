a, b = 0, 0
while True:
    if a >= 100 and a < 1000 and b >= 100 and b < 1000:
        break
    a, b = map(int, input().split())


b = str(b)

i = 1
list1 = [a * int(i) for i in b[::-1]]

for num in list1:
    print(num)

total = 0

for num in list1:
    total += num * i
    i *= 10

print(total)