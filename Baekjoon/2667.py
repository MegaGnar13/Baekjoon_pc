A=int(input())
map=[list(map(int,input())) for i in range(A)]
# print(map)

dx=[0,0,1,-1]
dy=[1,-1,0,0]
answer=[]
def BFS(map,a,b):
    count=0
    queue=[]
    n=len(map)
    queue.append([a,b])
    map[a][b]=0
    while queue:
        x=queue.pop(0)
        count+=1

        for i in range(4):
            nx=x[0]+dx[i]
            ny=x[1]+dy[i]

            if nx<0 or ny<0 or nx>n-1 or ny>n-1:
                continue
            else:
                if map[nx][ny]==1:
                    map[nx][ny]=0
                    queue.append([nx,ny])
    answer.append(count)


for i in range(A):
    for j in range(A):
        if map[i][j]==1:
            BFS(map,i,j)

answer.sort()
print(len(answer))
for i in answer:
    print(i)