x,y,z = map(int,input().split())

hiding = int(input())

spots = []


for i in range(hiding):
    spot = list(map(int,input().split()))
    spots.append(spot)

for i in range(len(spots)):
    if spots[i] == [x,y,z]:
        spots[i] = 0.0
        # print(1)
    elif spots[i][2] == z:
        spots[i] = abs((((spots[i][0]-x)**2 + (spots[i][1]-y)**2)**0.5)/2)
        # print(2)

    elif z > spots[i][2]:
        spots[i] = abs((((spots[i][0]-x)**2 + (spots[i][1]-y)**2)**0.5)/2) + abs(spots[i][2] - z)
        # print(3)

    else:
        tempa = (spots[i][2]-z)/4
        # print(tempa)
        tempb = (((spots[i][0]-x)**2 + (spots[i][1]-y)**2)**0.5)
        if tempa*3 >= tempb:
            spots[i] = tempa
            # print(4)

        else:
            spots[i] = tempa + (tempb - tempa*3)/2
            # print(5)
 

final = min(spots)

if final.is_integer():
    print(int(final))
else:
    print(final)

#15/15 done