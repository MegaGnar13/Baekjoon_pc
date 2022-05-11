import sys
test = int(input())

for _ in range(test):
    length = int(input())
    sticker = [list(map(int, sys.stdin.readline().split())) for i in range(2)]

    # print(sticker)

    target = [[0 for i in range(length)] for j in range(2)]

    for i in range(length):
        if i == 0:
            target[0][i] = sticker[0][i]
            target[1][i] = sticker[1][i]

        elif i == 1:
            target[0][i] = target[1][i-1] + sticker[0][i]
            target[1][i] = target[0][i-1] + sticker[1][i]

        else:
            target[0][i] = max(target[1][i-2], target[1][i-1]) + sticker[0][i]
            target[1][i] = max(target[0][i-2], target[0][i-1]) + sticker[1][i]

    e1 = target[0][-1]
    e2 = target[1][-1]
    print(max(e1,e2))