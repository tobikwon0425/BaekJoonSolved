N = int(input())

for i in range(N)[::-1]:
    
    for j in range(N):
        if j >= i:
            print("*", end="", flush=True)
        else:
            print(" ", end="", flush=True)
    print()
