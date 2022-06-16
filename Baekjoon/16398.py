import sys
n = int(input())

planet = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

flow = []

parent = [i for i in range(n)]

def find(k):
    if parent[k] != k:
        parent[k] = find(parent[k])

    return parent[k]

def union(a, b):
    first = find(a)
    second = find(b)

    if first < second:
        parent[second] = first
    else:
        parent[first] = second


for i in range(n):
    for j in range(n):
        flow.append([planet[i][j],i,j])

flow.sort()

# print(flow)

ans = 0
for i in flow:
    if find(i[1]) != find(i[2]):
        ans += i[0]
        union(i[1], i[2])

print(ans)