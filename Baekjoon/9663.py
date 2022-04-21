n = int(input())

queen = [0 for i in range(n)]

dfs = []
ans = 0
def queens(m):
    # print(dfs)
    global ans
    if len(dfs) == n:
        ans += 1
        return

    for i in range(n):

        err = 0
        for k in dfs:

            if k[1] == i or abs(m-k[0]) == abs(i-k[1]):
                err+=1
                break
        if err == 0:
            dfs.append([m,i])

            queens(m+1)
            dfs.pop()

queens(0)
print(ans)