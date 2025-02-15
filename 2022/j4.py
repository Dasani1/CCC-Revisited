together = []
cantbe = []
groups = []
violations = 0

x = int(input())
for i in range(x):
    tg = list(input().split())
    together.append(tg)

y = int(input())
for i in range(y):
    nt = list(input().split())
    cantbe.append(nt)

x_vio = [0]*x
y_vio = [0]*y

g = int(input())
for i in range(g):
    group = list(input().split())
    groups.append(group)

last = -1
if x > y:
    dom = x #shhhh
else:
    dom = y

for i in range(g):
    for j in range(dom):
        if x == dom:
            if together[j][0] not in groups[i] or together[j][1] not in groups[i]:
                if x_vio[j] == 0:
                    violations += 1
                    print(together[j][0],together[j][1])
                x_vio[j] += 1
            if j < y-1:
                if cantbe[j][0] in groups[i] or cantbe[j][1] in groups[i]:
                    if y_vio[j] == 0:
                        violations += 1
                        print(cantbe[j][0],cantbe[j][1])
                    y_vio[j] += 1
        else:
            if j < x-1:
                if together[j][0] not in groups[i] or together[j][1] not in groups[i]:
                    if x_vio[j] == 0:
                        violations += 1
                        print(together[j][0],together[j][1])
                    x_vio[j] += 1
            if cantbe[j][0] in groups[i] or cantbe[j][1] in groups[i]:
                if y_vio[j] == 0:
                    violations += 1
                    print(cantbe[j][0],cantbe[j][1])
                y_vio[j] += 1

print(violations)

#3/15


