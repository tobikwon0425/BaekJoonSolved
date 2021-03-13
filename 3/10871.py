N, X = map(int, input().split())

list1 = list(map(int, input().split()))

list2 = [list1[i] for i in range(N) if list1[i] < X]

for num in list2:
    print(num, end= " ", flush= True)