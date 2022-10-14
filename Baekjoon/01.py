from collections import deque
import sys

height, width = map(int, sys.stdin.readline().split())

m = []

for i in range(height):
    m.append(list(input()))


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def hole(x, y):
    tmp_r = [[0 for i in range(width)] for j in range(height)]

    queue = deque([[x,y,'0']])
    tmp_r[x][y] = 1

    while queue:
        tmp = queue.popleft()

        if m[tmp[0]][tmp[1]] == 'O':
            return tmp[2][1:]

        for l in range(4):
            nx = tmp[0] + dx[l]
            ny = tmp[1] + dy[l]

            if 0 <= nx <= height-1 and 0 <= ny <= width - 1 and (m[nx][ny] == '.' or m[nx][ny] == 'O') and tmp_r[nx][ny] == 0:
                tmp_r[nx][ny] = 1

                if l == 0:
                    if tmp[2][-1] == 'r':
                        queue.append([nx, ny, tmp[2]])
                    else:
                        tmp[2] += 'r'
                        queue.append([nx, ny, tmp[2]])
                elif l == 1:
                    if tmp[2][-1] == 'l':
                        queue.append([nx, ny, tmp[2]])
                    else:
                        tmp[2] += 'l'
                        queue.append([nx, ny, tmp[2]])

                elif l == 2:
                    if tmp[2][-1] == 'u':
                        queue.append([nx, ny, tmp[2]])
                    else:
                        tmp[2] += 'u'
                        queue.append([nx, ny, tmp[2]])

                else:
                    if tmp[2][-1] == 'd':
                        queue.append([nx, ny, tmp[2]])
                    else:
                        tmp[2] += 'd'
                        queue.append([nx, ny, tmp[2]])

    return tmp[2][1:]

red = []
blue = []
h = []
for i in range(height):
    for j in range(width):
        if m[i][j] == 'R':
            red = [i, j]
        if m[i][j] == 'B':
            blue = [i, j]
            a = hole(i, j)
        if m[i][j] == 'O':
            h = [i,j]
print(a)
print(red)
print(blue)
print(h)

for t in range(len(a)):
    if a[t] == 'l':
        if red[0] == blue[0] and red[1] < blue[1]:







if len(a) < 1 or len(a) > 10:
    print(-1)
else:
    print(len(a))

