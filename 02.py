import sys
A = int(sys.stdin.readline())
graph_list = []
for i in range(A):
    B=list(map(int,sys.stdin.readline().split()))

    B.reverse()
    graph_list.append(B)

graph_list.sort()
for i in range(len(graph_list)):
    a=graph_list[i]
    print(a[1],a[0])
