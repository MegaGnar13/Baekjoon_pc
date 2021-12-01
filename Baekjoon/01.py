def solution (n,hori):
    m=[[0 for i in range(n)] for j in range(n)]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    m[0][0]=1
    point = 2
    while m[0][n-1]==0 or m[n-1][0]==0:
        if hori == True and point ==2:
            m[0][1]=2
            start=[0,1]
            point +=1
        elif hori == False and point ==2:
            m[1][0]=2
            start=[1,0]
            point +=1
        nd = []
        for i in range(4):
            nx=start[0]+dx[i]
            ny=start[1]+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            else:
                if m[nx][ny]==0:
                    nd.append([nx,ny,max(nx,ny)])
        nd.sort(key=lambda x:x[2])
        m[nd[0][0]][nd[0][1]]=point
        point+=1
        start=[nd[0][0],nd [0][1]]
    print(m)
solution(5,False)