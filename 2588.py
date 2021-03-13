a, b = map(int, input().split())

b = str(b)

total = 0
i = 1

for num in b[::-1]:
    num = int(num)
    print(a * num)
    total += a * num * i
    i *= 10

print(total)