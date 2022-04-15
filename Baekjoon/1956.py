import heapq
import sys
# node, edges = map(int,input().split())
#
# n = {}
#
# for i in range(1,node+1):
#     n[i] = {}
#
# for i in range(edges):
#
#     start, end, weight = map(int,sys.stdin.readline().split())
#
#     if end in n[start]:
#         if n[start][end] > weight:
#             n[start][end] = weight
#
#     else:
#         n[start][end] = weight
#
#
# def dijstra(s):
#
#     ans = [float('inf') for i in range(node+1)]
#
#     queue = [[0,s]]
#     ans[s] = 0
#
#     while queue:
#
#         target = heapq.heappop(queue)
#
#         for des in n[target[1]]:
#             new_des = des
#             new_dis = ans[target[1]] + n[target[1]][des]
#
#             if new_dis < ans[new_des]:
#                 ans[new_des] = new_dis
#
#                 heapq.heappush(queue,[new_dis,new_des])
#
#     return ans
# e = {}
# for i in range(1,node+1):
#     total = dijstra(i)
#     e[i] = total
#
# # print(e)
#
# ans = float('inf')
#
# for num in e:
#     for i in range(num+1, len(e[num])):
#         if e[num][i] != float('inf') and e[i][num] != float('inf'):
#             if e[num][i] + e[i][num] < ans:
#                 ans = e[num][i] + e[i][num]
# print(ans)
#

# V: 마을 갯수, E: 도로 갯수
V, E = map(int, sys.stdin.readline().split())

INF = sys.maxsize
arr = [[INF for _ in range(V)] for _ in range(V)]

for _ in range(E):
    i, j, c = map(int, sys.stdin.readline().split())
    arr[i-1][j-1] = c

for k in range(V):  # 거쳐가는애
    for i in range(V):  # from
        for j in range(V):  # to
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

result = INF
#  계속 갱신한 뒤 사이클은 본인부터 본인까지에 저장됨
for i in range(V):
    result = min(result, arr[i][i])

if result == INF:
    print(-1)
else:
    print(result)