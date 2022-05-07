a, b = map(int, input().split())

cnt = 1

while a != b and b > a:
    if b%2 == 0:
        b //= 2
        cnt += 1

    else:
        if b%10 == 1:
            b //= 10
            cnt += 1
        else:
            break

if a == b:
    print(cnt)
else:
    print(-1)