from collections import deque
import sys
y, x =map(int,sys.stdin.readline().split())

m=[]
for _ in range(y):
   m.append(list(map(int,list(sys.stdin.readline().rstrip()))))

nm = [[[] for _ in range(x)] for i in range(y)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    queue=deque([[0,0,1,0]])
    m[0][0] = 1
    while queue:
        # print(queue)
        a=queue.popleft()

        if a[0] == y-1 and a[1] == x-1:
            return a[3]+1


        for _ in range(4):
            nx = a[1]+dx[_]
            ny = a[0]+dy[_]

            if 0<=nx<=x-1 and 0<=ny<=y-1 and a[2] not in nm[ny][nx]:
                if m[ny][nx] == 0:
                    queue.append([ny, nx, a[2], a[3]+1])

                    nm[ny][nx].append(a[2])
                else:
                    if a[2] == 0:
                        continue
                    else:
                        queue.append([ny, nx, 0, a[3]+1])
                        nm[ny][nx].append(a[2])


a = bfs()
if a:
    print(a)
else:
    print(-1)
