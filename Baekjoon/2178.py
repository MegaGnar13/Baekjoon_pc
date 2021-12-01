x,y=map(int,input().split())
mapmap=[list(map(int,input())) for i in range(x)]
map_1=[]
map_2=[]
for i in mapmap:
    map_1.append(i.copy())
    map_2.append(i.copy())
answer=[]
s = [[0]*y for i in range(x)]
s[0][0]=1
def fright(x,y):
    count=0
    dx=[0,-1,1,0]
    dy=[-1,0,0,1]
    stack=[[x,y]]
    map_1[x][y]=0
    while stack:
        next=stack.pop(0)
        # print(next[0],next[1])
        count+=1
        # if next[0]==len(map_1)-1 and next[1]==len(map_1[0])-1:
        #     break
        for i in range(4):
            nx=dx[i]+next[0]
            ny=dy[i]+next[1]
            if nx<0 or ny<0 or nx>=len(map_1)or ny>=len(map_1[0]):
                continue
            if map_1[nx][ny] == 1:
                stack.append([nx, ny])
                map_1[nx][ny] = 0
                s[nx][ny] = s[next[0]][next[1]] + 1

    answer.append(count)

# def fdown(map,x,y):
#     count=0
#     dx=[0,-1,0,1]
#     dy=[-1,0,1,0]
#     stack=[[x,y]]
#     map[x][y]=0
#     while stack:
#         next=stack.pop()
#         # print(next[0], next[1])
#         count+=1
#         if next[0]==len(map)-1 and next[1]==len(map[0])-1:
#             break
#         for i in range(4):
#             nx=dx[i]+next[0]
#             ny=dy[i]+next[1]
#             if nx<0 or ny<0 or nx>=len(map)or ny>=len(map[0]):
#                 continue
#             if map[nx][ny]==1:
#                 stack.append([nx,ny])
#                 map[nx][ny]=0
#     answer.append(count)

fright(0,0)
# fdown(mapmap,0,0)
# print(min(answer))
# print(s)
print(s[len(map_1)-1][len(map_1[0])-1])
