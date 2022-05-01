import sys
from collections import deque

n = int(input())

tree = {}

for i in range(1, n+1):
    tree[i] = {}

for _ in range(n):

    a = list(map(int, sys.stdin.readline().split()))

    start = a[0]

    ends = a[1:-1]

    for j in range(len(ends)//2):
        end = ends[2*j]
        weight = ends[2*j+1]

        if end in tree[start]:
            if weight < tree[start][end]:
                tree[start][end] = weight

        else:
            tree[start][end] = weight

        if start in tree[end]:
            if weight < tree[end][start]:
                tree[end][start] = weight


def bfs(start):

    ans = [0 for i in range(n+1)]
    queue = deque([[0, 0, start]])

    real_ans = []

    while queue:
        a = queue.popleft()

        if ans[a[2]] == 0:
            ans[a[2]] = 1

            real_ans.append(a)

            for i in tree[a[2]]:

                queue.append([a[0]+1, a[1]+tree[a[2]][i], i])


    real_ans.sort(key=lambda x:[-x[1],-x[0]])
    return real_ans[0]

ans = bfs(1)
anss=bfs(ans[2])
print(anss[1])

# ansss = 0
# node = 0
#
# for kkk in range(1, n+1):
#     ans = bfs(kkk)
#     if ansss < ans[1]:
#         ansss = ans[1]
#         node = ans[2]
#
# real = bfs(node)
#
# print(real[1])