import sys
from collections import deque
test = int(input())

for _ in range(test):
    n = int(input())
    ranked = list(map(int, sys.stdin.readline().split()))

    check = [0 for k in range(n+1)]
    check_out = [0 for k in range(n+1)]

    change = int(input())

    nm = {}
    for j in range(1, n+1):
        nm[j] = {}


    for i in range(change):
        a, b = map(int, sys.stdin.readline().split())

        if ranked.index(a) < ranked.index(b):
            check[a] += 1
            check_out[b] += 1
            nm[b][a] = 1
        else:
            check[b] += 1
            nm[a][b] = 1
            check_out[a] += 1
    ans = [0 for i in range(n)]

    queue = deque([])

    # print(check)
    # for i in range(1, len(check)):
    #     if check[i] == 0:
    #         queue.append(i)
    #
    # while queue:
    #     tar = queue.popleft()
    #     ans.append(tar)
    #
    #     for l in nm[tar]:
    #         check[l] -= 1
    #         if check[l] == 0:
    #             queue.appendleft(l)
    # print(ans)


    # for i in range(len(ranked)):
    #     tar = ranked[i]
    #
    #     if check[tar] == 0:
    #         ans.append(tar)
    #
    #         cc = 0
    #         for l in nm[tar]:
    #             check[l] -= 1
    #             if check[l] == 0:
    #                 cc += 1
    #
    #
    #                 ans.append(l)
    #
    # print(ans)

    dd = {}
    for i in range(len(ranked)):
        tar = ranked[i]
        dd[tar] = i + check[tar] - check_out[tar]

    # print(dd)

    s = set()
    for kkk in dd:
        s.add(dd[kkk])
        ans[dd[kkk]] = kkk

    # print(len(s))
    # print(ans)
    if len(s) == n:
        print(*ans)
    else:
        print("IMPOSSIBLE")