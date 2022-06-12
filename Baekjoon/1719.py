import sys

node, edge = map(int, sys.stdin.readline().split())

inf = 1e9

m = [[inf for i in range(node)] for j in range(node)]
ans = [['-' for ii in range(node)] for jj in range(node)]


for i in range(edge):
    a, b, weight = map(int, sys.stdin.readline().split())

    if m[a-1][b-1] > weight:
        m[a-1][b-1] = weight
        ans[a-1][b-1] = b
    if m[b-1][a-1] > weight:
        m[b-1][a-1] = weight
        ans[b-1][a-1] = a

# print(m)
# print(ans)

for i in range(1, node + 1):
    for j in range(1, node + 1):
        for k in range(1, node + 1):
            if i != j and i != k and j != k:
                if m[j-1][k-1] > m[j-1][i-1] + m[i-1][k-1]:
                    m[j-1][k-1] = m[j-1][i-1] + m[i-1][k-1]
                    ans[j-1][k-1] = ans[j-1][i-1]
# print(m)
# print(ans)

for i in ans:
    print(*i)