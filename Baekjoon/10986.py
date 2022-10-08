n, m = map(int, input().split())
li = list(map(int, input().split()))

prefix = 0

tmp = [0 for i in range(m)]

for i in range(n):
    prefix += li[i]

    t = prefix % m
    tmp[t] += 1

# print(tmp)

ans = 0
for i in tmp:
    ans += (i*(i-1))//2
ans += tmp[0]
# print(tmp)
print(ans)