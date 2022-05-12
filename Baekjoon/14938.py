import sys
import heapq

region, target, road = map(int,sys.stdin.readline().split())

node = {}

for i in range(1,region+1):
    node[i] = {}

item = list(map(int, sys.stdin.readline().split()))

for i in range(road):
    a, b, w = map(int, sys.stdin.readline().split())

    if b in node[a]:
        if node[a][b] > w:
            node[a][b] = w
    else:
        node[a][b] = w

    if a in node[b]:
        if node[b][a] > w:
            node[b][a] = w
    else:
        node[b][a] = w


def djistra(start):


    ans = [1e9 for i in range(region+1)]
    queue = [[0, start]]
    ans[start] = 0

    while queue:
        # print(queue)
        temp = heapq.heappop(queue)



        for i in node[temp[1]]:
            new_dis = temp[0] + node[temp[1]][i]
            new_des = i

            if ans[new_des] > new_dis:
                ans[new_des] = new_dis
                heapq.heappush(queue,[new_dis,new_des])

    return ans[1:]

total = 0

# print(item)
for i in range(1,region+1):
    answer = 0
    ars = djistra(i)
    for j in range(len(ars)):
        if ars[j] <= target:
            answer += item[j]
    # print(answer)
    if total < answer:
        total = answer

print(total)
