players = int(input())
total = 0
for i in range(players):
    score = int(input())
    foul = int(input())
    if (score*5)-(foul*3) > 40:
        total += 1

if total == players:
    print(total,end="+")
else:
    print(total)