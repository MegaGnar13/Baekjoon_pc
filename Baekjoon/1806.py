import sys
num, tar = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

prefix = [0]

presum = 0
for i in li:
    presum += i
    prefix.append(presum)
# print(prefix)


left = 0
right = 1
ans = 1e10

while left < right and right <= num:

    if -prefix[left] + prefix[right] < tar:
        right += 1

    else:
        if right - left < ans:

            ans = right - left
        # print(right, left)
        left += 1
if ans == 1e10:
    print(0)
else:
    print(ans)