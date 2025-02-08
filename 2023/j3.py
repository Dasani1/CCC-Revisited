people = int(input())

available = [0]*5

for i in range(people):
    schedule = list(input())
    for j in range(5):
        if schedule[j] == "Y":
            available[j] += 1

highest = max(available)
possible = []

for i in range(5):
    if available[i] == highest:
        possible.append(str(i+1))

print(",".join(possible))
    
