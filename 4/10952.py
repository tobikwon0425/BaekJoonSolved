sum_list = []

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    
    sum_list.append(a + b)
    

for sum_num in sum_list:
    print(sum_num)