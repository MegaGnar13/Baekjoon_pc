import sys
n = int(input())

stars = []

for i in range(n):
    x, y = map(float, sys.stdin.readline().split())

    stars.append([x, y, i])

# print(stars)

length = []
for i in range(n):
    for j in range(i+1, n):
        s1 = stars[i]
        s2 = stars[j]

        r = ((s1[0]-s2[0])**2 + (s1[1]-s2[1])**2)**0.5


        length.append([round(r, 2),s1[2],s2[2]])

# print(length)
length.sort()
# print(length)

check = [i for i in range(n)]

ans = 0

def find(a):
    if check[a] != a:
        check[a] = find(check[a])


    return check[a]

for w, start, end in length:
    if find(start) != find(end):
        ans += w

        if check[start] < check[end]:
            check[check[end]] = check[start]

        else:
            check[check[start]] = check[end]

print(ans)

