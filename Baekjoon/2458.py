import sys
N, M = map(int, sys.stdin.readline().split())

inf = 10e9
warshall = [[inf for i in range(N+1)] for j in range(N+1)]

for i in range(N+1):
    warshall[i][i] = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    warshall[a][b] = 1


for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if i != j and i != k and j != k:
                if warshall[j][k] > warshall[j][i] + warshall[i][k]:
                    warshall[j][k] = warshall[j][i] + warshall[i][k]

# print(warshall[1:])

tar = [True] * (N+1)
for i in range(1,N+1):
    for j in range(i,N+1):
        if warshall[i][j] == inf:
            if warshall[j][i] == inf:
                tar[i], tar[j] = False, False

print(tar.count(True)-1)
