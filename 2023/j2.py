peppers = int(input())
total = 0

for i in range(peppers):
    pepper = input()

    if pepper == "Poblano":
        total += 1500
    elif pepper == "Mirasol":
        total += 6000
    elif pepper == "Serrano":
        total += 15500
    elif pepper == "Cayenne":
        total += 40000
    elif pepper == "Thai":
        total += 75000
    elif pepper == "Habanero":
        total += 125000
        
print(total)