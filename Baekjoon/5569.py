w, h = map(int, input().split())

dp = [[[0 for i in range(4)] for j in range(w+1)] for l in range(h+1)]


for i in range(2, h+1):
    dp[i][2][1] = 1
    dp[i][2][3] = 1

for i in range(2, w+1):
    dp[2][i][0] = 1
    dp[2][i][2] = 1

for i in range(3, h+1):
    for j in range(3, w+1):
        first = dp[i][j-1]

        f_rr = first[0]
        f_ur = first[1]
        f_ru = first[2]
        f_uu = first[3]

        dp[i][j][0] += f_rr
        dp[i][j][0] += f_ur
        dp[i][j][1] += f_uu

        second = dp[i-1][j]

        s_rr = second[0]
        s_ur = second[1]
        s_ru = second[2]
        s_uu = second[3]

        dp[i][j][2] += s_rr
        dp[i][j][3] += s_ru
        dp[i][j][3] += s_uu

# print(dp)

# print(dp[h][w])

print(sum(dp[h][w]) % 100000)