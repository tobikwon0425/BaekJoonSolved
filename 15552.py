import sys

t = int(sys.stdin.readline())
sum_list = []

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    sum_list.append(a + b)

for sum_num in sum_list:
    print(sum_num)    