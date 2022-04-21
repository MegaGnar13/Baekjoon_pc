import sys

N, M = map(int, sys.stdin.readline().split())

n = [[0 for i in range(N+1)] for j in range(N+1)]

s = []
for _ in range(N):

    s.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        n[i+1][j+1] = n[i][j+1] + n[i+1][j] - n[i][j] + s[i][j]

# print(n)
for i in range(M):

    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())

    ans = n[x2][y2]-n[x1-1][y2]-n[x2][y1-1]+n[x1-1][y1-1]
    print(ans)

