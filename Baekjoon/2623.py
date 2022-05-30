import sys
from collections import deque
node, chance = map(int, sys.stdin.readline().split())

n = {}

for i in range(1, node + 1):
    n[i] = {}

check = [0 for i in range(node + 1)]

total = []



for i in range(chance):
    a = list(map(int, sys.stdin.readline().split()))
    many = a[0]

    for k in range(1, many):
        first = a[k]
        second = a[k + 1]

        if second not in n[first]:
            check[second] += 1
            n[first][second] = 1

# print(check)

queue = deque([])
for i in range(1, len(check)):
    if check[i] == 0:
        queue.append(i)

ans = []
while queue:
    a = queue.popleft()
    ans.append(a)

    for i in n[a]:
        check[i] -= 1
        if check[i] == 0:
            queue.append(i)

if len(ans) == node:
    for i in ans:
        print(i)
else:
    print(0)