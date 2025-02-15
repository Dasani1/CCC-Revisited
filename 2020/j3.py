max_x = 0
max_y = 0
min_x = 200
min_y = 200
for i in range(int(input())):
    x,y = map(int,input().split(","))

    if x > max_x:
        max_x = x

    if y > max_y:
        max_y = y

    if x < min_x:
        min_x = x
    
    if y < min_y:
        min_y = y

print(min_x-1,min_y-1,sep=",")
print(max_x+1,max_y+1,sep=",")

