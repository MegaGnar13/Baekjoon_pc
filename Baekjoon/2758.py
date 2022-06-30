import sys
sys.setrecursionlimit(int(1e5))
test = int(sys.stdin.readline())

def call(now_index, num):

    ans = 0

    if now_index == 1:
        ans += num
        return ans

    tar = 2 ** (now_index-1)

    for i in range(tar, num + 1):

        if i in dd[now_index]:
            ans += dd[now_index][i]
        else:
            dd[now_index][i] = call(now_index - 1, i // 2)
            ans += dd[now_index][i]


    return ans

dd = {}
for i in range(11):
    dd[i] = {}

for _ in range(test):

    n, m = map(int, sys.stdin.readline().split())


    answer = call(n, m)

    print(answer)

