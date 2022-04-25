import sys
# num, m = map(int,sys.stdin.readline().split())
num = 2
m = int(input())
NM = [[1,1],[1,0]]
#
# for _ in range(num):
#     NM.append(list(map(int,sys.stdin.readline().split())))


def matrix(U, V):
    n = len(U)
    Z = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1_000_000_007

    return Z

def mmmm(NM, m):

    if m == 1:
        for x in range(num):
            for j in range(num):
                NM[x][j] %= 1_000_000_007
        return NM

    tmp = mmmm(NM, m//2)

    if m%2 == 0:
        return matrix(tmp, tmp)
    else:
        return matrix(matrix(tmp, tmp), NM)

ans = mmmm(NM, m)

print(ans[0][1])