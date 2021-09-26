A, B = map(int,input().split())

visited = [False]*A
out=[]

def NM(depth,A,B):
    if depth == B:
        print(' '.join(map(str,out)))
        return
    for i in range(len(visited)):
        if visited[i] == True:
            continue
        else:
            visited[i]=True
            out.append(i+1)
            NM(depth+1,A,B)
            visited[i]=False
            out.pop()




NM(0,A,B)