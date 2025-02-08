tune = input()
word = ""
state = False
test = []
for char in tune:
    if char == "+":
        print(f"{word} tighten ",end="")
        word = ""
    elif char == "-":
        print(f"{word} loosen ",end="")
        word = ""
    elif char.isnumeric():
        test.append(char)
        word += char
        state = True
    elif not char.isnumeric() and state:
        print(word)
        state = False
        word = ""
        word += char
    else:
        word += char

print(word)




