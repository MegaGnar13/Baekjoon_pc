from collections import deque
import sys

num = int(input())
ans = 0
same = []

for _ in range(num):
    a = int(input())
    same.append(a)

target = same.copy()
target = list(set(target))
target.sort()
target = deque(target)

while len(same) > 1:
    temp = []
    for i in range(len(same)-1):
        if i != len(same)-1:
            if same[i] == same[i+1]:
                temp.append(i)

    for i in range(len(temp)):
        same.pop(temp[i]-i)

    if len(same) == 1:
        break

    for i in range(len(same)):

        if same[i] == target[0]:
            if i == 0:
                ans += same[1] - same[i]
                same[i] = same[1]

            elif i == len(same) - 1:
                ans += same[-2] - same[-1]
                same[i] = same[-2]

            else:
                first = same[i-1]
                second = same[i+1]

                if first < second:
                    ans += first - same[i]
                    same[i] = first
                else:
                    ans += second - same[i]
                    same[i] = second
    target.popleft()
    # print(same)
print(ans)