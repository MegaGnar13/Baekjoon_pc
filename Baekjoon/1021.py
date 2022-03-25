import collections
import sys
total, num = map(int,sys.stdin.readline().split())
tar = list(map(int, sys.stdin.readline().split()))

circle = collections.deque(_+1 for _ in range(total))

cnt = 0
for _ in tar:

    a = circle.index(_)
    b = len(circle) - a

    if a<=b:

        for i in range(a):
            x = circle.popleft()
            circle.append(x)
            cnt+=1
        circle.popleft()
    else:
        for i in range(b):
            x = circle.pop()
            circle.appendleft(x)
            cnt+=1
        circle.popleft()

print(cnt)