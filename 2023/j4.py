size = int(input())

row1 = list(map(int,input().split()))
row2 = list(map(int,input().split()))

total = 0

for i in range(size): #6/15 points
    if row1[i] == 1 and row2[i] == 1 and i % 2 == 0:
        total -= 2

    if row1[i-1] == 1 and row1[i] == 1 and i != 0:
        total += 1
    elif row1[i] == 1:
        total += 3

    if row2[i-1] == 1 and row2[i] == 1 and i != 0:
        total += 1
    elif row2[i] == 1:
        total += 3



print(total)