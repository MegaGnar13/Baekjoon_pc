import sys

row, column = map(int, sys.stdin.readline().split())

block = list(map(int, sys.stdin.readline().split()))

tar = block[0]
ans = 0

temp = []

for i in range(1, len(block)):

    if i == len(block) - 1:
        end = block[-1]

        if end < tar:

            for j in range(len(temp)-1, -1, -1):
                if temp[j] < end:
                    ans += end - temp[j]


                else:
                    end = temp[j]

        else:

            ans += (len(temp) * tar - sum(temp))

        break

    if block[i] < tar:
        temp.append(block[i])
    else:
        m = min(tar, block[i])

        l = len(temp)

        ans += m*l - sum(temp)

        tar = block[i]
        temp = []

print(ans)