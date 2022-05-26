from collections import deque
num = int(input())

check = [0 for i in range(num+1)]

node = {}

for i in range(1,num+1):
    node[i] = {}


for i in range(num-2):
    a, b = map(int, input().split())

    node[a][b] = 1
    node[b][a] = 1


def bfs(start):
    queue = deque([start])
    check[start] = 1

    while queue:
        a = queue.popleft()

        for i in node[a]:
            if check[i] == 0:
                check[i] = 1
                queue.append(i)

bfs(1)
# print(check)
print(1,end = " ")

for i in range(1,num+1):
    if check[i] == 0:
        print(i)
        break