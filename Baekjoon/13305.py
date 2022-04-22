num = int(input())

kilo = list(map(int,input().split()))
oil = list(map(int,input().split()))

tar = oil[0]
ans = oil[0] * kilo[0]
for i in range(num-2):
    if oil[i+1] < tar:
        tar = oil[i+1]

    ans += tar * kilo[i+1]

print(ans)
