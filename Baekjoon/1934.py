n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    aa = a
    bb = b

    while True:
        if a > b:
            next = a % b

            if next == 0:
                break

            a = b
            b = next

        else:

            next = b % a

            if next == 0:
                break

            b = next

    # print(min(a,b))
    ans = min(a,b)
    print(aa//ans * bb//ans * ans)