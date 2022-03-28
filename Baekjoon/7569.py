import sys
import collections

x, y, z = map(int,sys.stdin.readline().split())
m=[]

for _ in range(z):
    t= []
    for k in range(y):
        t.append(list(map(int,sys.stdin.readline().split())))
    m.append(t)

start = []

for k in range(z):
    for i in range(y):
        for j in range(x):
            if m[k][i][j] == 1:
                start.append([j,i,k,0])


dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(start):
    tt= []
    queue = collections.deque(start)
    while queue:
        a = queue.popleft()
        tt.append(a[3])
        for _ in range(6):
            nx = a[0]+dx[_]
            ny = a[1]+dy[_]
            nz = a[2]+dz[_]
            if 0<=nx<=x-1 and 0<=ny<=y-1 and 0<=nz<=z-1 and m[nz][ny][nx] == 0:
                queue.append([nx,ny,nz,a[3]+1])
                m[nz][ny][nx] = 1
    return tt[-1]

if start:
    a= bfs(start)
else:
    a=0


err = 0
for k in range(z):
    for i in range(y):
        for j in range(x):
            if m[k][i][j] == 0:
                err+=1
if err==0:
    print(a)
else:
    print(-1)