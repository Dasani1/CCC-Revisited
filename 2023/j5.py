word = input()

rows = int(input())
col = int(input())

grid = []

for i in range(rows):
    letters = list(input().split())
    grid.append(letters)


print(grid)
    