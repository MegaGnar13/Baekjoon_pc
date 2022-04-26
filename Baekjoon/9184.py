import sys

n = [[[0 for i in range(21)] for k in range(21)] for l in range(21)]

def fun(a,b,c):
    if a <= 0 or b <= 0 or c <=0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return fun(20, 20, 20)
    else:
        if n[a-1][b][c] == 0:
            first = fun(a-1, b, c)
            n[a-1][b][c] = first
        else:
            first = n[a-1][b][c]

        if  n[a-1][b-1][c] == 0:
            second = fun(a-1,b-1,c)
            n[a-1][b-1][c] = second
        else:
            second = n[a-1][b-1][c]

        if n[a-1][b][c-1] == 0:
            third = fun(a-1,b,c-1)
            n[a - 1][b][c - 1] = third
        else:
            third = n[a-1][b][c-1]

        if n[a-1][b-1][c-1] == 0:
            fourth = fun(a-1, b-1, c-1)
            n[a-1][b-1][c-1] = fourth
        else:
            fourth = n[a-1][b-1][c-1]

        return  first + second + third - fourth




while True:
    a,b,c = map(int, sys.stdin.readline().split())

    if a== -1 and b== -1 and c == -1:
        break

    ans = fun(a,b,c)

    print(f'w{a, b, c} = {ans}')
