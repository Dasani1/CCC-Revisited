ask = int(input())
scores = []
singles = []
counter = 0

for i in range(ask):
    score = int(input())
    if score not in scores:
        singles.append(score)
    scores.append(score)

singles.sort(reverse=True)
third = singles[2]

for points in scores:
    if points == third:
        counter += 1

print(third,counter)
#13/15 too inefficient...