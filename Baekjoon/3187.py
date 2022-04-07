import sys
from collections import deque

xx, yy = map(int,sys.stdin.readline().split())

village = []
for i in range(xx):
    village.append(sys.stdin.readline().rstrip())

num_village = []

for i in range(xx):
    row = []
    for j in range(yy):
        if village[i][j] == '#':
            row.append(1)
        else:
            row.append(0)
    num_village.append(row)



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

v_num = 0
k_num = 0

def bfs(x, y):
    global v_num,k_num
    global village

    tv_num = 0
    tk_num = 0

    queue = deque([[x,y]])
    num_village[x][y] = 1
    while queue:

        a = queue.popleft()

        if village[a[0]][a[1]] == 'v':
            tv_num += 1
        elif village[a[0]][a[1]] == 'k':
            tk_num += 1

        for _ in range(4):

            nx = dx[_] + a[0]
            ny = dy[_] + a[1]

            if 0 <= nx <= xx-1 and 0 <= ny <= yy-1:
                if  num_village[nx][ny] == 0:
                    num_village[nx][ny] = 1
                    queue.append([nx, ny])

    if tv_num >= tk_num:
        v_num += tv_num
    else:
        k_num += tk_num


for i in range(xx):
    for j in range(yy):
        if num_village[i][j] == 0:
            bfs(i,j)

print(k_num)
print(v_num)
