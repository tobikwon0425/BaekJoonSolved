def max(array: list)-> tuple:
    max = -1
    index = 0

    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            index = i
    
    return max, index + 1

array = []

for i in range(9):
    array.append(int(input()))

max, index = max(array)

print(max, index)