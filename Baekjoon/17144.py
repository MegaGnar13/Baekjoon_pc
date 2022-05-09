import sys
x, y, s = map(int, sys.stdin.readline().split())

room = []

for i in range(x):
    r = list(map(int, sys.stdin.readline().split()))
    room.append(r)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dust():
    target = [[0 for i in range(y)] for j in range(x)]
    for i in range(x):
        for j in range(y):
            if room[i][j] > 0:
                next = room[i][j] // 5
                tar = 0
                for l in range(4):
                    nx = i + dx[l]
                    ny = j + dy[l]

                    if 0 <= nx <= x-1 and 0 <= ny <= y-1 and room[nx][ny] != -1:

                        target[nx][ny] += next
                        tar += 1

                target[i][j] -= next*tar
    for i in range(x):
        for j in range(y):
            room[i][j] += target[i][j]

def cleaner():
    ac = []
    for i in range(x):
        for j in range(y):
            if room[i][j] == -1:
                ac.append([i,j])

    fx, fy = ac[0]

    for i in range(fx-1, 0, -1):
        room[i][0] = room[i-1][0]

    for i in range(y-1):
        room[0][i] = room[0][i+1]

    for i in range(fx):
        room[i][y-1] = room[i+1][y-1]

    for i in range(y-1, 1, -1):
        room[fx][i] = room[fx][i-1]

    room[fx][1] = 0

    ex, ey = ac[1]

    for i in range(ex+1, x-1):
        room[i][0] = room[i+1][0]
    for i in range(y-1):
        room[x-1][i] = room[x-1][i+1]
    for i in range(x-1, ex, -1):
        room[i][y-1] = room[i-1][y-1]
    for i in range(y-1, 1, -1):
        room[ex][i] = room[ex][i-1]

    room[ex][1] = 0

for i in range(s):
    dust()
    cleaner()
# print(room)

answer = 0
for i in range(x):
    for j in range(y):
        if room[i][j] > 0:
            answer += room[i][j]
print(answer)