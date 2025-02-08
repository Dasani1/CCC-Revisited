expected = input()
actual = input()

correct = "-"
silent = "-"
silly = "-"
possible = []

if len(actual) == len(expected): #3 points
    silent = "-"
    for i in range(len(expected)):
        if expected[i] != actual[i]:
            correct = expected[i]
            silly = actual[i]
            break
else:
    for i in range(len(actual)):
        pass