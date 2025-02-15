p = int(input())
n = int(input())
r = int(input())

total = n
days = 0
infected = n

while(total <= p):
    days += 1

    infected = infected * r
    total += infected
    

    
    

print(total)
print(days)



