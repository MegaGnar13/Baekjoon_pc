import sys

node, origin = map(int, sys.stdin.readline().split())

coordinate = []

check = [i for i in range(node+1)]

def find(n):
    if check[n] != n:
        check[n] = find(check[n])

    return check[n]

for _ in range(node):
    x, y = map(float, sys.stdin.readline().split())

    coordinate.append([x, y])

for _ in range(origin):
    n1, n2 = map(int, sys.stdin.readline().split())

    # if find(n1) != find(n2):

    if check[n1] < check[n2]:
        check[check[n2]] = check[n1]
    else:
        check[check[n1]] = check[n2]

nodes = []

for i in range(len(coordinate)):
    for j in range(i+1, len(coordinate)):
        x1, y1 = coordinate[i]
        x2, y2 = coordinate[j]

        weight = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        nodes.append([weight, i+1, j+1])

nodes.sort()

# print(nodes)

ans = 0
for w, n1, n2 in nodes:
    if find(n1) != find(n2):

        ans += w

        if check[n1] < check[n2]:
            check[check[n2]] = check[n1]
        else:
            check[check[n1]] = check[n2]

# print(check)
print(f'{ans:.2f}')