import sys
from collections import deque
ladder, snake = map(int, input().split())

worp = {}

for i in range(ladder+snake):
    start, end = map(int, input().split())
    worp[start] = end

def bfs():

    answer = [0 for i in range(101)]
    answer[0] = 1

    queue = deque([[1,0]])
    answer[1] = 1

    while queue:
        a = queue.popleft()

        for i in range(1,7):
            if answer[a[0]+i] == 0:
                answer[a[0]+i] = 1
                if a[0]+i in worp:
                    next = worp[a[0]+i]
                    if next == 100:
                        return a[1]+1


                    if answer[next] == 0:
                        answer[next] =1
                        queue.append([next,a[1]+1])


                else:
                    if a[0]+i == 100:
                        return a[1] + 1
                    queue.append([a[0]+i,a[1]+1])

aa = bfs()
print(aa)