#dfs and bfs
node,edge,start_point = map(int,input().split())
edge_list=[list(map(int,input().split())) for j in range(edge)]
next_node=dict()
for i in range(1,node+1):
    connect=[]
    for j in edge_list:
        if i in j:
            j.remove(i)
            connect.extend(j)
            j.append(i)
            connect.sort()
    next_node[i]=connect

def DFS(next_node,startpoint):

    stack=[]
    answer=[]
    stack.append(startpoint)
    while stack:
        n=stack.pop()
        if n not in answer:
            answer.append(n)
            stack.extend(reversed(next_node[n]))
    print(*answer)
    return
DFS(next_node,start_point)

def BFS(next_node,startpoint):
    queue=[]
    answer=[]
    queue.append(startpoint)
    while queue:
        n=queue.pop(0)
        if n not in answer:
            answer.append(n)
            queue.extend(next_node[n])
    print(*answer)
    return
BFS(next_node,start_point)