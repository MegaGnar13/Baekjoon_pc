import sys

num = int(sys.stdin.readline())

M = [0,0,0]
m = [0,0,0]

for i in range(num):
    first, second, third = map(int,sys.stdin.readline().split())
    for j in range(3):
        if j == 0:
            a = max(M[0], M[1]) + first
            aa = min(m[0], m[1]) + first

        elif j == 1:
            b = max(M[0], M[1], M[2]) + second
            bb = min(m[0], m[1], m[2]) + second

        else:
            c = max(M[1], M[2]) + third
            cc = min(m[1], m[2]) + third

    M[0] = a
    M[1] = b
    M[2] = c

    m[0] = aa
    m[1] = bb
    m[2] = cc
print(max(M),end=" ")
print(min(m))