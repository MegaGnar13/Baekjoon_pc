xx = {}
yy = {}
for _ in range(3):
    x, y = map(int, input().split())
    if x in xx:
        xx[x]+=1
    else:
        xx[x]=1
    if y in yy:
        yy[y]+=1
    else:
        yy[y]=1

ans_x = 0
ans_y = 0
for i in xx:
    if xx[i] == 1:
        ans_x = i
for j in yy:
    if yy[j] == 1:
        ans_y = j

print(ans_x,ans_y)