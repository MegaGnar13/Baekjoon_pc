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

stack = deque([[start,1]])


check = [0 for i in range(n+1)]

while stack:
    tar = stack.pop()

    if check[tar[0]] == 0:
        check[tar[0]] = tar[1]

        for i in node[tar[0]]:
            stack.append([i,tar[1]+1])

# print(check)

for i in range(1,len(check)):
    print(check[i])