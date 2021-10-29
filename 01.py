import sys
A,B,C = map(int,sys.stdin.readline().split())
mark=[list(map(int,sys.stdin.readline().split())) for i in range(A)]
set_mark=set()
for i in mark:
    set_mark.update(i)
answer=[]
for height in set_mark:
    num=0
    block=C
    for x in range(A):
        for y in range(B):
            if mark[x][y]>height:
                num+=(mark[x][y]-height)*2
                block-=1
            elif mark[x][y]<height:
                num+=(height-mark[x][y])
                block-=1
            else:
                continue
    if block>=0:
        answer.append([num,height])
answer.sort(key=lambda x:(x[0],x[1]))
print(*answer[0])