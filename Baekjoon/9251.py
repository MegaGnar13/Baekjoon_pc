import sys
first = ' '+input()
second = ' '+input()

# print(first)
# print(second)
n = [[0 for i in range(len(first))] for j in range(len(second))]

ans = 0

for i in range(1, len(second)):
    for j in range(1, len(first)):
        # print(i,j)
        if second[i] == first[j]:
            n[i][j] = min(n[i-1][j], n[i][j-1]) + 1
            # n[i][j] = n[i-1][j-1] + 1

            if ans < n[i][j]:
                ans = n[i][j]
        else:
            n[i][j] = max(n[i-1][j], n[i][j-1])


print(ans)


