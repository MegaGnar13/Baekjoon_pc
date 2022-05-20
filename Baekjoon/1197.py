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
    # print(check,'before find', tar)
    if find(check, n1) != find(check, n2):
        # print(check,'after find')
        ans += tar
        if check[n1] < check[n2]:           # 중요 !!! 최고 조상의 조상을 바꿔야한다!
            check[check[n2]]= check[n1]
        else:
            check[check[n1]] = check[n2]

        # union(check, n1, n2)


    # print(check,'end',n1,n2)
    # print(check,tar)

# print(check)
print(ans)