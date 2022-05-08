import sys

a, b = map(int, sys.stdin.readline().split())

first = list(map(int, sys.stdin.readline().split()))
second = list(map(int, sys.stdin.readline().split()))

se = {}
for i in second:
    se.setdefault(i,1)

ans = 0

for i in first:
    if i in se:
        ans+=1

print(len(first) + len(second) - 2*ans)