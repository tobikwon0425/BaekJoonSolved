sum_list = []

while True:
    try:
        a, b = map(int, input().split())
        sum_list.append(a + b)
    except:
        break

for sum_num in sum_list:
    print(sum_num)