import sys
node, edge = map(int, sys.stdin.readline().split())

weight = []

for i in range(edge):
    a, b, w = map(int, sys.stdin.readline().split())

    weight.append([w, a, b])

weight.sort()

check = [i for i in range(node+1)]
# print(check)
def find(li, a):
    if li[a] != a:
        li[a] = find(li, li[a])

    return li[a]

def union(li, a, b):
    a = find(li, a)
    b = find(li, b)

    if a > b:
        li[a] = b
    else:
        li[b] = a

ans = 0
# print(weight)

for tar, n1, n2 in weight:

    if find(check, n1) != find(check, n2):
        ans += tar
        union(check, n1, n2)


    # print(check,tar)

# print(check)
print(ans)