x,y = map(int,input().split()) #x=세로 y=가로
map=[list(map(int,input())) for i in range(x)]
s=[]
for i in map:
    s.append(map.copy())
def fast():
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    lenx=len(map)
    leny=len(map[0])

    queue=[[0,0,1]]
    map[0][0]=11
    s[0][0]==11
    while queue:
        next=queue.pop(0)

        for i in range(4):
            nx=dx[i]+next[0]
            ny=dy[i]+next[1]


            if nx<0 or ny<0 or nx>=lenx or ny>=leny:
                continue

            if map[nx][ny]==0:
                s[nx][ny]=s[next[0]][next[1]]+1
                queue.append([nx,ny,next[2]])

            # if len(queue)==0 and onecount==1:
            if next[2]==1 and map[nx][ny]==1:
                nx+=dx[i]
                ny+=dy[i]
                if nx < 0 or ny < 0 or nx >= lenx or ny >= leny:
                    continue
                if map[nx][ny] == 0:
                    s[nx][ny] = s[next[0]][next[1]] + 2
                    queue.append([nx, ny,0])

fast()
print(map)
if map[len(map)-1][len(map[0])-1]==0:
    print(-1)
else:
    print(map[len(map)-1][len(map[0])-1]-10)
