import sys

n = int(input())

bi = list(map(int, sys.stdin.readline().split()))

def bitonic(bi):

    dp = []

    for i in range(len(bi)):
        ans = 1
        for j in range(i):
            if bi[j] < bi[i] and dp[j] >= ans:
                ans = dp[j] + 1

        dp.append(ans)

    return dp

a = bitonic(bi)

bi.reverse()

b = bitonic(bi)

# print(a)
# print(b)
tar_1 = a.index(max(a))
tar = len(b) - b.index(max(b)) - 1
b.reverse()

ans = 0
for i in range(len(a)):
    if a[i] + b[i] > ans:
        ans = a[i] + b[i]

print(ans - 1)
# print(max(a[tar_1]+b[tar_1]-1, a[tar]+b[tar]-1))



