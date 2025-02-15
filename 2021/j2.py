max = 0
person = ""
for i in range(int(input())):
    name = input()
    price = int(input())
    if price > max:
        max = price
        person = name

print(person)