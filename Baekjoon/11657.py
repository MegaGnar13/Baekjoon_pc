import sys
import heapq

node, edge = map(int,sys.stdin.readline().split())

n={}
for i in range(1,node+1):
    n[i] = {}

for i in range(edge):
    start, end, weight = map(int,sys.stdin.readline().split())
    if end in n[start]:
        if n[start][end]>weight:
            n[start][end] = weight
    else:
        n[start][end] = weight

ans = [float('inf')] * (node + 1)

def ballman(sss):
    ans[sss] = 0

    for i in range(node):

        for m in n:
            for connect in n[m]:
                new_des = connect
                new_dis = ans[m] + n[m][connect]

                if ans[m] != float('inf') and new_dis < ans[new_des]:

                    ans[new_des] = new_dis

                    if i == node-1:
                        return True
    return False

lll = ballman(1)
if lll:
    print(-1)
else:
    for i in range(2,len(ans)):
        if ans[i] == float('inf'):
            print(-1)
        else:
            print(ans[i])