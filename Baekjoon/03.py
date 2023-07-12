n, m = map(int,input().split())
chess = []
for i in range(n):
    chess.append(list(input()))

# print(chess)

ans = float('inf')

for i in range(n-7):
    for j in range(m-7):
        cnt = 0
        ccnt = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                # W start
                if (k+l)%2 == 1:
                    if chess[k][l] == 'W':
                        cnt += 1
                    if chess[k][l] == 'B':
                        ccnt += 1

                else:
                    if chess[k][l] == 'B':
                        cnt += 1
                    if chess[k][l] == 'W':
                        ccnt += 1
        if ans > min(cnt, ccnt):
            ans = min(cnt, ccnt)

print(ans)


