T = int(input())
sum_list = []

for _ in range(T):
    A, B = map(int, input().split())
    sum_list.append(A + B)

for i in range(len(sum_list)):
    print("Case #{}: {}".format(i+1, sum_list[i]))

