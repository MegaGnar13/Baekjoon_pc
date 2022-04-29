import sys

n = int(sys.stdin.readline())

sequence = list(map(int, sys.stdin.readline().split()))

target = int(sys.stdin.readline())

sequence.sort()

point1 = 0
point2 = n-1

ans = 0
while point1 < point2:
    tar = sequence[point1] + sequence[point2]

    if tar < target:
        point1 += 1

    elif tar > target:
        point2 -= 1
    else:
        ans += 1
        point1 += 1

print(ans)