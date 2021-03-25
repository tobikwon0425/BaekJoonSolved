def d(n: int) -> int:
    sum = n
    num_str = str(n)

    
    for num in num_str:
        sum += int(num)
    
    return sum

a = []

for i in range(1, 10001):
    a.append(d(i))

for i in range(1, 10001):
    if i in a:
        pass
    else:
        print(i)