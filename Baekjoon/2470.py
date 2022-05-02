import sys
num = int(input())

li = list(map(int, sys.stdin.readline().split()))

li.sort()

a = 0
b = num-1

ans = 1e10
anslit = []

while a < b:
    if abs(li[a] + li[b]) < ans:
        ans = abs(li[a] + li[b])
        anslit = [li[a], li[b]]

    if li[a] + li[b] < 0:
        a+=1

    else:
        b -= 1
anslit.sort()
print(*anslit)