import sys
num = int(input())

home = []

for _ in range(num):
    home.append(list(map(int, sys.stdin.readline().split())))
INF = 10e9

ans = 10e9

for i in range(3):
    np = [[INF, INF, INF] for j in range(num)]

    np[0][i] = home[0][i]

    for k in range(1, num):
        np[k][0] = min(np[k-1][1], np[k-1][2]) + home[k][0]
        np[k][1] = min(np[k-1][0], np[k-1][2]) + home[k][1]
        np[k][2] = min(np[k-1][0], np[k-1][1]) + home[k][2]

    for ll in range(3):
        if np[-1][ll] < ans and ll != i:
            ans = np[-1][ll]
print(ans)