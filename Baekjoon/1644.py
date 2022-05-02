import sys
import math
num = int(sys.stdin.readline())

def primeset(num):

    pr = [0 for i in range(num+1)]

    tar = int(math.sqrt(num))

    for i in range(2, tar+1):
        if pr[i] == 0:
            for j in range(i+i, num+1, i):
                pr[j] = 1

    return [i for i in range(2,num+1) if pr[i] == 0]

li = primeset(num)

# print(li)

prefix = [0]

presum = 0
for i in li:
    presum += i
    prefix.append(presum)
# print(prefix)


left = 0
right = 1
tar = num
ans = 0
num = len(prefix)-1
# print(prefix)

while left < right and right <= num:

    if -prefix[left] + prefix[right] < tar:
        right += 1

    elif -prefix[left] + prefix[right] > tar:
        left += 1
    else:
        # print(prefix[left], prefix[right])
        ans += 1
        left += 1

print(ans)