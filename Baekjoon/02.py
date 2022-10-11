import sys
tar = 0

def find(k):
    if check[k] != k:
        check[k] = find(check[k])

    return check[k]

def union(n, m):
    first = find(n)
    second = find(m)

    if first < second:
        check[second] = first
    else:
        check[first] = second

while True:
    tar += 1
    a, b = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0:
        break
    else:
        check = [i for i in range(a + 1)]
        same = []

        for _ in range(b):
            c, d = map(int, sys.stdin.readline().split())

            if find(c) != find(d):
                union(c, d)

            else:
                same.append(find(c))

        # print((check[1:]))
        # print(same)

        for i in range(1, a+1):
            check[i] = find(check[i])

        for j in range(len(same)):
            same[j] = find(same[j])

        # print((check[1:]))
        # print(same)

        ans = len(set(check[1:])) - len(set(same))

        if ans > 1:
            print(f"Case {tar}: A forest of {ans} trees.")
        elif ans == 1:
            print(f"Case {tar}: There is one tree.")
        else:
            print(f"Case {tar}: No trees.")
