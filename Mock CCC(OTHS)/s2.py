n = int(input())

shiro = list(map(int,input().split()))
shino = list(map(int,input().split()))

swaps = 0
positions = []

for i in range(n-1):
    if shiro == shino:
        break
    else:
        if shiro[i] != shino[i]:
            # print(shiro)
            temp = shiro[i]
            p2 = shiro[i::].index(shino[i])+i

            shiro[p2] = temp
            shiro[i] = shino[i]
            swaps += 1
            positions.append([i+1,p2+1])

if swaps == 0:
    print(0)
else:
    print(swaps)
    for i in range(len(positions)):
        print(*positions[i])

# print(shiro)