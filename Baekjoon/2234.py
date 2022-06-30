import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

castle = []

for i in range(m):
    castle.append(list(map(int, sys.stdin.readline().split())))

check = [[0 for i in range(n)] for j in range(m)]
start = 1
def bfs(x,y,start):
    check[x][y] = start
    queue = deque([[x,y,1]])
    tar = 1

    while queue:
        a = queue.popleft()

        word = bin(castle[a[0]][a[1]])
        word = word[2:]
        word = f'{word:0>4}'



        for i in range(1,5):
            if word[-i] == '0':
                if i == 1:
                    nx = a[0]
                    ny = a[1] - 1
                elif i == 2:
                    nx = a[0] - 1
                    ny = a[1]
                elif i == 3:
                    nx = a[0]
                    ny = a[1] + 1
                else:
                    nx = a[0] + 1
                    ny = a[1]

                if 0<= nx <= m-1 and 0<= ny <= n-1:
                    if check[nx][ny] == 0:
                        check[nx][ny] = start
                        queue.append([nx,ny,a[2]+1])
                        tar += 1

    st[start] = tar
    return tar

st = {}

width = 0
cnt = 0
total = 0

for i in range(m):
    for j in range(n):
        if check[i][j] == 0:
            cnt += 1
            tttt = bfs(i,j,start)
            width = max(width, tttt)
            start += 1
print(cnt)
print(width)
# print(check)
for i in range(m-1):
    for j in range(n-1):
        if check[i][j] != check[i+1][j]:
            temp = st[check[i][j]] + st[check[i+1][j]]
            total = max(total,temp)
        if check[i][j] != check[i][j+1]:
            temp2 = st[check[i][j]] + st[check[i][j+1]]
            total = max(total,temp2)

for ii in range(n-1):
    if check[-1][ii] != check[-1][ii+1]:
        temp = st[check[-1][ii]] + st[check[-1][ii+1]]
        total = max(total,temp)
for jj in range(m-1):
    if check[jj][-1] != check[jj+1][-1]:
        temp2 = st[check[jj][-1]] + st[check[jj+1][-1]]
        total = max(total,temp2)


print(total)
