s, N, K, R1, R2, C1, C2 = map(int, input().split())

m = [[0 for i in range(N**s)] for j in range(N**s)]

tar = N**s//N

def block(x1, y1, tmp):

    for i in range(tmp*K):
        for j in range(tmp*K):
            m[x1 + tmp + i][y1 + tmp + j] = 1

    if tmp == 1:
        return

    for i in range(N):
        for j in range(N):
            block(x1+tmp*i, y1+tmp*j, tmp//N)

block(0,0,tar)
for i in range(len(m)):
    print(''.join(map(str, m[i])))

print("------------------")

for i in range(R1, R2+1):
    print(''.join(map(str,m[i][C1:C2+1])))