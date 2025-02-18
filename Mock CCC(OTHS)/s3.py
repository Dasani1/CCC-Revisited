n,k = map(int,input().split())

leader = 0
controlled = [0]*k
strength = [0]*k

for i in range(n):
    l,w,s = map(int,input().split())
    for j in range(l,w):
        if s > strength[j]:
            strength[j] = s
            controlled[j] = i


    


        
print(controlled)
