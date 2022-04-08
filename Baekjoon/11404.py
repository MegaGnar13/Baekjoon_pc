import sys
import heapq

node = int(sys.stdin.readline())

edge = int(sys.stdin.readline())

n = {}
for i in range(1,node+1):
    n[i] = {}

for i in range(edge):
    a, b, weight = map(int,sys.stdin.readline().split())

    if b in n[a]:
        if n[a][b] > weight:
            n[a][b] = weight

    else:
        n[a][b] = weight

# print(n)

answer = []

def dijkstra(start):
    ans = [float('inf')] * (node+1)

    queue = [[0,start]]
    ans[start] = 0

    while queue:

        target = heapq.heappop(queue)
        for i in n[target[1]]:
            new_des = i
            new_dis = target[0] + n[target[1]][i]

            if new_dis < ans[new_des]:
                ans[new_des] = new_dis
                heapq.heappush(queue,[new_dis,new_des])

    for i in range(len(ans)):
        if ans[i] == float('inf'):
            ans[i] = 0
    return ans[1:]


for i in range(1,node+1):
    some = dijkstra(i)
    answer.append(some)


# print(answer)
for i in answer:
    print(*i)