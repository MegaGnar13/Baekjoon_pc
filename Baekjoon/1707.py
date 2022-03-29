import sys
from collections import deque

n = int(sys.stdin.readline())

def bfs(start):
    queue = deque([[start,1]])


    while queue:

        a = queue.popleft()

        if ans[a[0]] == 0:
            ans[a[0]] = a[1]
            if ed[a[0]]:
                for i in ed[a[0]]:
                    queue.append([i,a[1]*(-1)])
        else:
            if ans[a[0]]*(-1) == a[1]:
                return 'NO'

    return 'YES'


for _ in range(n):
    ed = {}
    node, edges = map(int,sys.stdin.readline().split())
    for l in range(1,node+1):
        ed[l] = []

    for i in range(edges):
        a, b =map(int,sys.stdin.readline().split())

        ed[a].append(b)
        ed[b].append(a)

    err = 0
    ans = [0 for _ in range(node + 1)]
    for _ in range(1,node+1):

        if ans[_] == 0:
            a=bfs(_)
            if a == 'NO':
                err+=1
                print('NO')
                break

    if err == 0:
        print('YES')
    # else:
    #     print('NO')