n = int(input())
testcase = []
score_list = []

for i in range(n):
    testcase.append(input())

for i in range(len(testcase)):
    score_list.append(0)
    count = 0
    
    for char in testcase[i]:
        if char == "O":
            count += 1
            score_list[i] += count
        else:
            count = 0

for score in score_list:
    print(score)