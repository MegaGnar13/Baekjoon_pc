from collections import deque
n, k = map(int, input().split())

m = []

for _ in range(n):
    m.append(list(map(int, input().split())))

s, end_x, end_y = map(int,input().split())

t = []

for i in range(n):
    for j in range(n):
        if m[i][j] != 0:
            t.append([m[i][j], i, j,  0])

t.sort()

tmp = deque(t)

# print(tmp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


while True:
    if not tmp:
        break

    next = tmp.popleft()

    if next[3] == s:
        break

    for _ in range(4):

        n_x = dx[_] + next[1]
        n_y = dy[_] + next[2]

        if 0 <= n_x <= n-1 and 0 <= n_y <= n-1 and m[n_x][n_y] == 0:
            m[n_x][n_y] = next[0]

            tmp.append([next[0], n_x, n_y, next[3]+1])

# print(end_x, end_y)
print(m[end_x-1][end_y-1])