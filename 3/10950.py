from collections import deque

T = int(input())
list1 = deque()

for i in range(T):
    num1, num2 = map(int, input().split())
    list1.append(num1 + num2)

for item in list1:
    print(item)
