import sys
n = int(input())
pe = list(map(int,sys.stdin.readline().split()))
con = list(map(int,sys.stdin.readline().split()))

b=sum(con)
cc = []
for i in range(len(con)):
    nxt = [i] * con[i]
    cc.extend(nxt)

# print(cc)


ans = []
tar = []
for i, j in enumerate(cc):
    tar.append([i,j])
# print(tar)
us = []

def nm(a, b):
    if len(us) == b:
        cmd = []
        for k in us:
            cmd.append(k[1])
        # if cmd not in ans:
        cmd= tuple(cmd)
        ans.append(cmd)
        return
    for i in range(len(tar)):
        if tar[i] in us:
            continue
        us.append(tar[i])
        nm(i,b)
        us.pop()
nm(0,b)

# print(set(ans))
ans = set(ans)
# print(len(ans))

ans_M = 0
ans_m = 1000000000000


for i in ans:
    tar = 0
    for j in range(len(i)):
        if j == 0:
            if i[j] == 0:
                tar = pe[j] + pe[j+1]
            elif i[j] == 1:
                tar = pe[j] - pe[j+1]
            elif i[j] == 2:
                tar = pe[j] * pe[j+1]
            elif i[j] == 3:
                if pe[j] < 0:
                    tar = -(-pe[j]//pe[j+1])
                else:
                    tar = pe[j]//pe[j+1]
        else:
            if i[j] == 0:
                tar += pe[j+1]
            elif i[j] == 1:
                tar -= pe[j+1]
            elif i[j] == 2:
                tar *= pe[j+1]
            elif i[j] == 3:
                if tar < 0:
                    tar = -(-tar//pe[j+1])
                else:
                    tar = tar//pe[j+1]

    if tar < ans_m:
        ans_m = tar
    if tar > ans_M:
        ans_M = tar
print(ans_M)
print(ans_m)


