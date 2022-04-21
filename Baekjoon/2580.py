import sys

dp = []

for i in range(9):
    dp.append(list(map(int,sys.stdin.readline().split())))

num = [1,2,3,4,5,6,7,8,9]

zero = []
for i in range(9):
    for j in range(9):
        if dp[i][j] == 0:
            zero.append([i,j])


ans = []

def row(tar, co):
    x = co[0]
    y = co[1]

    target = dp[x]

    if tar in target:
        return 1
    else:
        return 0

def column(tar ,co):
    x = co[0]
    y = co[1]
    ans = 0
    for i in range(9):
        if dp[i][y] == tar:
            ans+=1
    return ans

def cluster(tar, co):
    x = (co[0] // 3) * 3
    y = (co[1] // 3) * 3
    ans = 0
    for i in range(3):
        for j in range(3):
            if dp[x+i][y+j] == tar:
                ans += 1

    return ans
end = 0
def zeros(n):
    global end
    # print(dp)
    if len(ans) == len(zero):
        end+=1
        for mmm in dp:
            print(*mmm)

        return

    for i in num:
        next = zero[n]

        n1 = row(i,next)
        if n1 != 0:
            continue

        n2 = column(i,next)
        if n2 != 0:
            continue
        n3 = cluster(i,next)
        if n3 != 0:
            continue
        # print(i, next, n1, n2, n3)


        ans.append(next)
        dp[next[0]][next[1]] = i
        zeros(n+1)

        if end > 0:
            return

        dp[next[0]][next[1]] = 0
        ans.pop()



zeros(0)
