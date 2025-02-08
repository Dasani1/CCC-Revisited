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
    for char in actual:
        if char not in expected:
            silly = char
            break
    for char in expected:
        if char not in actual and char not in possible:
            possible.append(char)
    testing = expected.replace(possible[0],"")
    testing = testing.replace(possible[1],silly)

    if "".join(testing) == actual:
        correct = possible[1]
        silent = possible[0]
    else:
        correct = possible[0]
        silent = possible[1]

# print(testing)
# print(possible)
# print(expected)
print(correct,silly)
print(silent) 

