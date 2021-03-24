n = int(input())

grade_list = []
list1 = []
for i in range(n):
    score_list = list(map(int, input().split()))
    grade_list.append(score_list)

for grade in grade_list:
    avg = sum(grade[1:]) / grade[0]
    count = 0
    
    for score in grade[1:]:
        if avg < score:
            count += 1

    list1.append(count / grade[0] * 100)
    
for num in list1:
    print("{0:.3f}%".format(round(num, 3)))
    

