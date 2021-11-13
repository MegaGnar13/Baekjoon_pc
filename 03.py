from collections import deque

def bfs(start, end,n,link_arr):
    q = deque()
    q.append(start)
    visit = [-1] * (n + 1)
    visit[start] = 0
    while q:
        cur = q.popleft()
        if cur == end: break
        for adj_node, adj_dist in link_arr[cur]:
            if visit[adj_node] > -1: continue
            visit[adj_node] = visit[cur] + adj_dist
            q.append(adj_node)
    return visit[end]

def solution(n, edges):
    answer = 0
    link_arr = [list() for _ in range(n)]
    for i in edges:
        n1, n2, w = i[0],i[1],1
        link_arr[n1].append((n2, w))
        link_arr[n2].append((n1, w))
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if bfs(x,y,n,link_arr)+bfs(y,z,n,link_arr)==bfs(x,z,n,link_arr) and x!=y and y!=z and z!=x:
                    answer+=1
    return answer
print(solution(4,[[2,3],[0,1],[1,2]]))