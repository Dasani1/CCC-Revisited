ask = int(input())
scores = []
counter = 0
counters = 0
top = -1
third = -1
second = -1 #Every number is a non-negative integer, this ensures the number will be atleast something on the list

for i in range(ask):
    score = int(input())
    if score > top:
        top = score #Find max first for efficiency
    scores.append(score)
    
scores.sort(reverse=True)

for points in scores:
    if counter == 2 and points == third:
        counters += 1
    elif points != top and counter == 0:
        counter += 1
        second = points
    elif points != second and counter == 1:
        counter += 1
        third = points
        counters += 1

print(third,counters)
# print(scores)

#test case section
# print("\n")
# print(top)
# print(second)
# print(third)
# print(counters)
# print(scores)

#15/15 done






