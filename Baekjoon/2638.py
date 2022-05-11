from collections import deque
x, y = map(int,input().split())

m = [list(map(int, input().split())) for i in range(x)]

ans = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def changem():
    start = deque([[0,0]])
    m[0][0] = 3

    temp_m = [[0 for i in range(y)] for j in range(x)]


    while start:
        a = start.popleft()

        for i in range(4):
            nx = a[0] + dx[i]
            ny = a[1] + dy[i]

            if 0 <= nx <= x-1 and 0 <= ny <= y-1 and m[nx][ny] != 1 and temp_m[nx][ny] == 0:
                if m[nx][ny] == 0:
                    m[nx][ny] = 3
                temp_m[nx][ny] = 1
                start.append([nx,ny])

def check():
    for i in range(x):
        for j in range(y):
            if m[i][j] == 1:
                tar = 0

                for l in range(4):
                    nx = i + dx[l]
                    ny = j + dy[l]

                    if m[nx][ny] == 3:
                        tar += 1

                if tar >= 2:
                    m[i][j] = 2

def delete():
    for i in range(x):
        for j in range(y):
            if m[i][j] == 2:
                m[i][j] = 3

def end():
    err = 0
    for i in range(x):
        if err > 0:
            break

        for j in range(y):
            if m[i][j] == 1:
                err += 1
                break

    if err > 0:
        return False
    else:
        return True

while True:
    changem()
    check()
    delete()
    if not end():
        ans += 1
        continue
    else:
        ans += 1
        break

print(ans)