books = list(input())
counter = 0 
l = books.count("L")
m = books.count("M")
s =books.count("S")

for i in range(l):
    if books[i] != "L":
        counter += 1

for i in range(l,l+m):
    if books[i] == "S":
        counter += 1

#LMSLMSLMLSLML
#Swaps in L range = 3
#Swaps in M Range

print(l)
print(m)
print(s)
print(counter)
