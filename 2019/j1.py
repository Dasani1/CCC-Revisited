apple = 0
banana = 0

a3 = int(input())*3
a2 = int(input())*2
a1 = int(input())
apple = a3+a2+a1

b3 = int(input())*3
b2 = int(input())*2
b1 = int(input())
banana = b3+b2+b1

if apple == banana:
    print("T")
elif apple > banana:
    print("A")
else:
    print("B")
