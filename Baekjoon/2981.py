from math import sqrt
n = int(input())

num = []
a=0
for i in range(n):
    a = int(input())
    num.append(a)
num.sort()

for i in range(n-1):
    num[i] = num[i+1] - num[i]
num.pop()
# print(num)

def uclid(a, b):
    while True:
        if a> b:
            next = a%b
            if next == 0:
                return b

            a = b
            b = next

        else:
            next = b % a
            if next == 0:
                return a

            b = next

for i in range(n-2):
    a = num.pop()
    b = num.pop()

    next = uclid(a, b)
    num.append(next)

# print(num)
tar = num[0]
ans = []
nx = int(sqrt(num[0]))
# print(nx)
for i in range(2, nx+1):
    if tar % i == 0:
        ans.append(i)
# print(ans)
for i in range(len(ans)):
    ans.append(tar//ans[i])

ans.append(tar)

ans = list(set(ans))
ans.sort()
print(*ans)
