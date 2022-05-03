nn = int(input())

tar = 2 * nn - 1

n = [[0 for i in range(tar)] for j in range(nn)]

def star(i, j, num):
    if num == 3:
        n[i][j] = 1
        n[i+1][j-1] = 1
        n[i+1][j+1] = 1
        n[i+2][j-2] = 1
        n[i+2][j-1] = 1
        n[i+2][j] = 1
        n[i+2][j+1] = 1
        n[i+2][j+2] = 1

    else:
        next = num//2

        star(i, j, next)

        star(i+next, j-next, next)
        star(i+next, j+next, next)

if nn == 3:
    star(0,2,nn)
else:
    star(0, nn-1, nn)

# print(n)


for i in range(len(n)):
    aans = ''
    for j in range(2*nn -1):
        if n[i][j] == 0:
            aans+=" "
        else:
            aans+="*"
    print(aans)


# print(ans)

# for i in n:
#     print(''.join(ans))
