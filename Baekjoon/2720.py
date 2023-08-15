Q = 25
D = 10
N = 5
P = 1

t = int(input())

for _ in range(t):

    target = int(input())

    q = target // Q

    target_2 = target-Q*q

    d = target_2 // D

    target_3 = target_2 - d*D

    n = target_3 // N

    target_4 = target_3 - n*N

    p = target_4 // P

    print(q, d, n ,p)