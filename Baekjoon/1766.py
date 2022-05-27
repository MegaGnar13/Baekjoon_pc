import heapq
import sys
node, edge = map(int, sys.stdin.readline().split())

n = {}
for i in range(1, node+1):
    n[i] = []

income = [0 for i in range(node + 1)]

for i in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    income[b] += 1
    n[a].append(b)

queue = []

for i in range(1, len(income)):
    if income[i] == 0:
        heapq.heappush(queue, i)

ans = []

while queue:
    a = heapq.heappop(queue)
    ans.append(a)
    for i in n[a]:
        income[i] -= 1
        if income[i] == 0:
            heapq.heappush(queue, i)

print(*ans)