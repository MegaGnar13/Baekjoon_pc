import sys
import copy
from collections import deque
n, m = map(int, sys.stdin.readline().split())

lab = []

for i in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    lab.append(li)

ans = []


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

rr = 0


def numzero(same_lab):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if same_lab[i][j] == 0:
                cnt += 1
    return cnt

def zeropadding():
    same_lab = copy.deepcopy(lab)
    # print(ans, same_lab)

    queue = deque([])

    for i in range(n):
        for j in range(m):
            if same_lab[i][j] == 2:
                queue.append([i, j])

    while queue:
        a = queue.popleft()
        for _ in range(4):

            nx = a[0] + dx[_]
            ny = a[1] + dy[_]

            #찾으면 바로 메꾸기
            if 0 <= nx < n and 0 <= ny < m and same_lab[nx][ny] == 0:
                same_lab[nx][ny] = 2
                queue.append([nx, ny])
    # print(same_lab)

    result = numzero(same_lab)
    # if result == 32:
    #     print(same_lab)

    return result

def dfs(start_x, start_y):
    # print(start_x, start_y)
    # print(ans)
    global rr

    if len(ans) == 3:
        num = zeropadding()
        if num > rr:
            rr = num
        return

    for i in range(start_x, n):
        if i == start_x:
            for j in range(start_y, m):
                if lab[i][j] == 0:
                    ans.append([i,j])
                    lab[i][j] = 1
                    dfs(i, j)
                    ans.pop()
                    lab[i][j] = 0
        else:
            for j in range(m):
                if lab[i][j] == 0:
                    ans.append([i,j])
                    lab[i][j] = 1
                    dfs(i, j)
                    ans.pop()
                    lab[i][j] = 0


dfs(0, 0)
print(rr)