import sys

test = int(input())


def find(name):
    if check[name][0] != name:
        check[name][0] = find(check[name][0])

    return check[name][0]


def union(n, m):
    first = find(n)
    second = find(m)

    tar = check[first][1] + check[second][1]
    if first < second:
        check[second] = [first, tar]
        check[first][1] = tar

    else:
        check[first] = [second, tar]
        check[second][1] = tar

    return tar

for _ in range(test):
    friend = int(input())

    check = {}

    for i in range(friend):

        a, b = input().split()

        if a not in check:
            check[a] = [a, 1]

        if b not in check:
            check[b] = [b, 1]

        if find(a) != find(b):
            ans = union(a, b)
        else:

            ans = check[check[a][0]][1]
        print(ans)


