import sys

computer = int(input())

parent = [i for i in range(computer+1)]

ans = 0
check = []

def find(k):
    if not parent[k] == k:
        parent[k] = find(parent[k])

    return parent[k]

def union(u, v):
    first = find(u)
    second = find(v)

    if first < second:
        parent[second] = first
    else:
        parent[first] = second

for i in range(computer):
    cc = list(input())

    for j in range(len(cc)):

        if cc[j] != "0":

            if i == j:
                if cc[j].islower():

                    ans += ord(cc[j]) - 96
                else:

                    ans += ord(cc[j]) - 38
            else:
                if cc[j].islower():
                    check.append([ord(cc[j])-96, i+1, j+1])
                else:
                    check.append([ord(cc[j])-38, i+1, j+1])

check.sort()

for i in range(len(check)):
    # print(check[i])

    if find(check[i][1]) != find(check[i][2]):
        union(check[i][1], check[i][2])
    else:
        ans += check[i][0]

err = 0
print(parent)
for i in range(1, computer):
    if parent[i] != parent[i+1]:
        err += 1
        break
if err == 0:
    print(ans)
else:
    print(-1)