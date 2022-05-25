import sys
test = int(input())

def find(v):
    if n[v] != v:
        n[v] = find(n[v])

    return n[v]


for _ in range(test):
    node, edge = map(int, sys.stdin.readline().split())

    ed = []
    for i in range(edge):
        ed.append(list(map(int, sys.stdin.readline().split())))

    n = [i for i in range(node+1)]

    ans = 0

    for v1, v2 in ed:
        if find(v1) != find(v2):
            ans += 1

            if n[v1] < n[v2]:
                n[n[v2]] = v1
            else:
                n[n[v1]] = v2

    print(ans)
