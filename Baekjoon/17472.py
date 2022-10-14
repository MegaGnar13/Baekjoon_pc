from collections import deque
n, m = map(int, input().split())

nara = []

for _ in range(n):
    nara.append(list(map(int, input().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j, w):
    queue = deque([[i, j]])
    nara[i][j] = w
    while queue:
        tmp = queue.popleft()

        for k in range(4):
            ni = tmp[0] + dx[k]
            nj = tmp[1] + dy[k]

            if 0 <= ni <= n-1 and 0 <= nj <= m-1 and nara[ni][nj] == 1:
                nara[ni][nj] = w
                queue.append([ni,nj])

start = 2

for i in range(n):
    for j in range(m):
        if nara[i][j] == 1:

            bfs(i, j, start)

            start+= 1

for i in nara:
    print(i)

# print(nara)

rqueue = []

for i in range(n):
    tmp = []
    t = {}
    for j in range(m):
        if nara[i][j] != 0:
            if nara[i][j] not in tmp:
                tmp.append(nara[i][j])

            if nara[i][j] not in t:
                t[nara[i][j]] = [j]

            else:
                t[nara[i][j]].append(j)

    if len(tmp) > 1:
        for l in range(len(tmp)-1):
            first = tmp[l]
            second = tmp[l + 1]
            w = t[second][0] - t[first][-1]
            if w - 1 > 1:
                rqueue.append([w-1, tmp[l], tmp[l+1]])

for j in range(m):
    tmp = []
    t = {}
    for i in range(n):
        if nara[i][j] != 0:
            if nara[i][j] not in tmp:
                tmp.append(nara[i][j])

            if nara[i][j] not in t:
                t[nara[i][j]] = [i]

            else:
                t[nara[i][j]].append(i)

    if len(tmp) > 1:
        for l in range(len(tmp)-1):
            first = tmp[l]
            second = tmp[l + 1]
            w = t[second][0] - t[first][-1]
            if w - 1 > 1:
                rqueue.append([w-1, tmp[l], tmp[l+1]])
print(rqueue)
rqueue.sort()
print(rqueue)
def find(a):
    if check[a] != a:
        check[a] = find(check[a])

    return check[a]

def union(u, v):
    first = find(u)
    second = find(v)

    if first < second:
        check[second] = first
    else:
        check[first] = second

# print(rqueue)

check = [i for i in range(start)]
ans = 0
for i in rqueue:
    if find(i[1]) != find(i[2]):
        ans += i[0]
        union(i[1], i[2])
for i in range(2, start):
    check[i] = find(check[i])

ccc = check[2:]

print(check)
if len(set(ccc)) == 1:
    print(ans)
else:
    print(-1)