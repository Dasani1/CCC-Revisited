word = input()

h = word.count("H")
v = word.count("V")

if h % 2 == 0 and v % 2 == 0:
    print(1,2)
    print(3,4)
elif h % 2 == 1 and v % 2 == 1:
    print(4,3)
    print(2,1)
elif h % 2 == 1 and v % 2 == 0:
    print(3,4)
    print(1,2)
else:
    print(2,1)
    print(4,3)

