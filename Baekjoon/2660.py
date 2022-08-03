import sys

n = int(input())

friend = {}

while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break

    else:
        if a in friend:
            friend[a][b] = 1
        else:
            friend[a] = {}
            friend[a][b] = 1

        if b in friend:
            friend[b][a] = 1
        else:
            friend[b] = {}
            friend[b][a] = 1

# print(friend)

base = [[float('inf') for i in range(n)] for j in range(n)]

for i in friend:
    for j in friend[i]:
        base[i-1][j-1] = 1

# print(base)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k:
                if base[j][k] > base[i][j] + base[i][k]:
                    base[j][k] = base[i][j] + base[i][k]

for i in range(n):
    base[i][i] = 0

# print(base)

temp = []

for i in base:
    temp.append(max(i))

tar = min(temp)

answer = []

for i in range(n):
    if temp[i] == tar:
        answer.append(i+1)

print(tar, len(answer))
print(*answer)