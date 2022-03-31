import heapq
import sys
N, E = map(int,sys.stdin.readline().split())

m = {}

for _ in range(1,N+1):
    m[_] = {}
for _ in range(E):
    a, b, w = map(int,sys.stdin.readline().split())

    m[a][b] = w
    m[b][a] = w

v1, v2 = map(int,sys.stdin.readline().split())



def mdistance(start):

    ans = [float('inf') for i in range(N + 1)]
    queue = [[0,start]]

    while queue:
        # print(queue)
        a = heapq.heappop(queue)

        if ans[a[1]] < a[0]:
            continue

        ans[a[1]] = a[0]

        for des, dis in m[a[1]].items():
            new_dis = dis + a[0]
            if ans[des] > new_dis:
                heapq.heappush(queue, [new_dis,des])
    return ans

first = mdistance(1)[v1] + mdistance(v1)[v2] + mdistance(v2)[N]
second = mdistance(1)[v2] + mdistance(v2)[v1] + mdistance(v1)[N]

if min(first,second) == float('inf'):
    print(-1)
else:
    print(min(first,second))
