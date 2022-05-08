import sys
from collections import deque
n, m, start = map(int, sys.stdin.readline().split())

node = {}
for i in range(1, n+1):
    node[i] = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    node[a].append(b)
    node[b].append(a)

stack = deque([start])


for k in node:
    node[k].sort(reverse=True)


check = [0 for i in range(n+1)]
ss = 0

while stack:

    tar = stack.pop()

    if check[tar] == 0:
        ss+=1
        check[tar] = ss

        for i in node[tar]:
            if check[i] == 0:
                stack.append(i)

# print(check)

for i in range(1,len(check)):
    print(check[i])