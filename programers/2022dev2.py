def solution(n, horizontal):

    temp = [[0 for i in range(n)] for j in range(n)]

    temp[0][0] = 1
    tar = 2
    now = 1
    next = 1

    while now < n:
        next += tar*now
        temp[now][now] = next

        now += 1
    # print(temp)

    if horizontal == False:
        for i in range(n):
            if i%2 == 0:
                for j in range(i):
                    standard = temp[i][i]
                    temp[i-j-1][i] = standard - j - 1
                    temp[i][i-j-1] = standard + j + 1
            else:
                for j in range(i):
                    standard = temp[i][i]
                    temp[i-j-1][i] = standard + j + 1
                    temp[i][i-j-1] = standard - j - 1
    else:
        for i in range(n):
            if i%2 == 0:
                for j in range(i):
                    standard = temp[i][i]
                    temp[i - j - 1][i] = standard + j + 1
                    temp[i][i - j - 1] = standard - j - 1
            else:
                for j in range(i):
                    standard = temp[i][i]
                    temp[i-j-1][i] = standard - j - 1
                    temp[i][i-j-1] = standard + j + 1

    return temp

solution(4, True)
