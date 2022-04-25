num = int(input())

stack = []

for _ in range(num):
    stack.append(int(input()))

n = 0
tar = []
ans = []
err = 0
for i in stack:
    if n < i:
        while n < i:
            n+=1
            tar.append(n)
            ans.append('+')
        ans.append('-')
        tar.pop()

    else:
        if i == tar[-1]:
            ans.append('-')
            tar.pop()
        else:
            err += 1
            break
# print(n)
# print(tar)
# print(ans)
# print(err)

if err > 0:
    print('NO')
else:
    for i in ans:
        print(i)

# print(tar)