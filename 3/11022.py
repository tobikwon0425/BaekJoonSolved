T = int(input())
element_list = []
sum_list = []

for _ in range(T):
    A, B = map(int, input().split())
    element_list.append((A, B))
    sum_list.append(A + B)

for i in range(len(sum_list)):
    A, B = element_list[i]
    print("Case #{}: {} + {} = {}".format(i+1, A, B,sum_list[i]))

