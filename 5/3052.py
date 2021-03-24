array = []

for i in range(10):
    array.append(int(input()) % 42)


for i in range(len(array)):
    j = i + 1
    while j < len(array):
        if array[i] == array[j]:
            del array[j]
        else:
            j += 1

print(len(array))