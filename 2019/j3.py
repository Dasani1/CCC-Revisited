num = int(input())

for i in range(num):
    code = input()
    counter = 0
    for i in range(len(code)): #if the character limit wasn't 80 I'd try to make it more efficient
        if i > 0 and code[i] != code[i-1]:
            print(counter,code[i-1], end=" ")
            counter = 1
        else:
            counter += 1
    
    print(counter,code[i])
        



    

