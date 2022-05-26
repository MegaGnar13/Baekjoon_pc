import sys
sys.setrecursionlimit(5000)
first = ' '+input()
second = ' '+input()

check = [[0 for i in range(len(first))] for j in range(len(second))]


for i in range(1, len(second)):
    for j in range(1, len(first)):
        if first[j] != second[i]:
            check[i][j] = max(check[i-1][j], check[i][j-1])
        else:
            check[i][j] = check[i-1][j-1] + 1

end = check[-1][-1]

ans = []

def checkss(a, b, tata):
    if len(ans) == end:
        return

    target = 0

    for j in range(b, -1, -1):

        if check[a][j] > max(check[a-1][j], check[a][j-1]) and check[a][j] == tata:
            ans.append(first[j])
            checkss(a-1, j-1, tata-1)
            target += 1
    if target == 0:
        checkss(a-1,b,tata)

checkss(len(second) - 1, len(first) - 1, end)
ans.reverse()
print(end)
print(''.join(ans))