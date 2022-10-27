num = int(input())
tmp = list(map(int, input().split()))
tar = int(input())

ans = {}

for i in range(len(tmp)):
    if tmp[i] not in ans:
        ans[tmp[i]] = 1
    else:
        ans[tmp[i]] += 1

if tar not in ans:
    print(0)
else:
    print(ans[tar])