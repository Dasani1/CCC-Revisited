previous = ""
while(True):
    direction = input()
    sum = (int(direction[0])+int(direction[1]))
    steps = direction[2]+direction[3]+direction[4]

    if direction == "99999":
        break
    else:
        if sum == 0:
            print(previous, steps)

        elif sum % 2 == 0:
            print("right",steps)
            previous = "right"
        elif sum % 2 == 1:
            print("left",steps)
            previous = "left"