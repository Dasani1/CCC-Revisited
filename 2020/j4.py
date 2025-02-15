word = input()
shift = input()

combinations = []
winner = False

for i in range(len(shift)):
    combinations.append(shift)
    shift = shift[1:]+shift[0]
    if combinations[i] in word:
        print("yes")
        winner = True
        break

if not winner:
    print("no")



