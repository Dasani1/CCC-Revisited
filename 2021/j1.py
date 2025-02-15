b = int(input())

if (b*5-400) == b:
    print(b)
    print(0)
elif (b*5-400) > b:
    print(b*5-400)
    print(-1)

else:
    print(b*5-400)
    print(1)