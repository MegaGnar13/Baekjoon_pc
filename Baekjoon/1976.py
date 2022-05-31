import sys

n = int(input())
total = int(input())

def find(k):
    if check[k] != k:
        check[k] = find(check[k])

    return check[k]


check = [i for i in range(n + 1)]

for i in range(n):
    tar = list(map(int, sys.stdin.readline().split()))

    for j in range(len(tar)):
        if tar[j] == 1:

            first = i + 1
            second = j + 1

            f = find(first)
            s = find(second)

            if f < s:
                check[s] = f
            else:
                check[f] = s

# print(check)

end = list(map(int, sys.stdin.readline().split()))

err = 0
for i in range(total-1):
    if find(end[i]) != find(end[i+1]):
        err += 1
        break

if err == 0:
    print("YES")
else:
    print("NO")