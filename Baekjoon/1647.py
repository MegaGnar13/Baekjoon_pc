import sys

node, edge = map(int, sys.stdin.readline().split())


def find(a):
    if check[a] != a:
        check[a] = find(check[a])

    return check[a]


roads = []

for i in range(edge):
    start, end, weight = map(int, sys.stdin.readline().split())

    roads.append([weight, start, end])

check = [i for i in range(node + 1)]

roads.sort()

total = 0
ans = 0

for i in roads:

    if find(i[1]) != find(i[2]):
        total += i[0]
        if ans < i[0]:
            ans = i[0]
        if check[i[1]] < check[i[2]]:
            check[check[i[2]]] = check[i[1]]
        else:
            check[check[i[1]]] = check[i[2]]

print(total - ans)

