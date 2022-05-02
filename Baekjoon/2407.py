n, m = map(int, input().split())

t = [[0 for i in range(n+1)] for j in range(n+1)]

def combination(n,m):
    if m == 1 or n-m == 1:
        t[n][m] = n
        return n
    elif m == 0 or m == n:
        t[n][m] = 1
        return 1

    else:

        first = t[n-1][m]
        second = t[n-1][m-1]

        if first == 0:
            first = combination(n-1, m)
            t[n-1][m] = first
        if second == 0:
            second = combination(n-1, m-1)
            t[n-1][m-1] = second

        return first + second

ans = combination(n, m)

print(ans)