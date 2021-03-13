n = input()

if int(n) < 10:
    n = n + "0"

counter = 0
truecase = n
while True:
     result = str(int(n[0]) + int(n[1]))
     compare = n[-1] + result[-1]
     counter += 1

     if truecase == compare:
         break
    
     n = compare
    
print(counter)