num = int(input())

n = []

for i in range(num):
    n.append(input())

# print(n)
answer = []

def quard(i,j,N):
    if N == 1:
        answer.append(n[i][j])
        return

    tar = n[i][j]
    err = 0
    for x in range(N):
        if err != 0:
            break
        for y in range(N):
            if n[i+x][j+y] != tar:
                err+=1
                break

    if err == 0:
        answer.append(tar)

    else:
        next = N//2
        answer.append('(')
        for x in range(2):
            for y in range(2):
                quard(i+next*x, j+next*y, next)
        answer.append(')')

quard(0,0,num)
print(''.join(answer))