from collections import deque
h, w = map(int, input().split())
m = []

for _ in range(h):
    m.append(list(input()))

r = []
b = []
hole = []
for i in range(h):
    for j in range(w):
        if m[i][j] == 'R':
            r = [i, j]
        if m[i][j] == 'B':
            b = [i, j]
        if m[i][j] == 'O':
            hole = [i, j]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0
err = 0
queue = deque([[r[0], r[1], b[0], b[1], cnt]])

tmp = [[[[0 for i in range(w)] for j in range(h)] for k in range(w)] for l in range(h)]
tmp[r[0]][r[1]][b[0]][b[1]] = 1

final = 0

while queue:

    next = queue.popleft()


    if next[4] > 10:
        err += 1
        break

    # print(next)

    if m[next[0]][next[1]] == 'O':
        if m[next[2]][next[3]] == 'O':
            continue
        else:
            final = next[4]
            break
    if m[next[2]][next[3]] == 'O':
        continue


    m[next[0]][next[1]] = 'R'
    m[next[2]][next[3]] = 'B'

    for i in range(4):

        start_red_x = next[0]
        start_red_y = next[1]

        red_x = next[0]
        red_y = next[1]

        end_red_x = 0
        end_red_y = 0

        while True:
            nx = red_x + dx[i]
            ny = red_y + dy[i]

            if m[nx][ny] == '.' or m[nx][ny] == 'B':
                red_x = nx
                red_y = ny
            elif m[nx][ny] == '#':
                end_red_x = red_x
                end_red_y = red_y
                break
            else:
                end_red_x = nx
                end_red_y = ny
                break

        start_blue_x = next[2]
        start_blue_y = next[3]

        blue_x = next[2]
        blue_y = next[3]

        end_blue_x = 0
        end_blue_y = 0

        while True:
            nx = blue_x + dx[i]
            ny = blue_y + dy[i]

            if m[nx][ny] == '.' or m[nx][ny] == 'R':
                blue_x = nx
                blue_y = ny
            elif m[nx][ny] == '#':
                end_blue_x = blue_x
                end_blue_y = blue_y
                break
            else:
                end_blue_x = nx
                end_blue_y = ny
                break



        if end_blue_y == end_red_y and end_blue_x == end_red_x and m[end_red_x][end_red_y] != 'O':
            if abs(end_blue_x - start_blue_x) + abs(end_blue_y - start_blue_y) > abs(end_red_x - start_red_x) + abs(end_red_y - start_red_y):

                end_blue_x -= dx[i]
                end_blue_y -= dy[i]
            else:
                end_red_x -= dx[i]
                end_red_y -= dy[i]

        if tmp[end_red_x][end_red_y][end_blue_x][end_blue_y] == 1:
            continue

        tmp[end_red_x][end_red_y][end_blue_x][end_blue_y] = 1
        queue.append([end_red_x, end_red_y, end_blue_x, end_blue_y, next[4] + 1])

    m[next[0]][next[1]] = '.'
    m[next[2]][next[3]] = '.'

    # print(queue)
if err == -1 or final == 0:
    print(-1)
else:
    print(final)