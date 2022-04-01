import sys
import heapq

total_case = int(input())

def shortest(start, end):
    ans = [float('inf') for num in range(n + 1)]
    queue = [[0, start]]
    ans[start] = 0

    while queue:

        # print(queue)
        a = heapq.heappop(queue)

        if ans[a[1]] < a[0]:
            continue

        for des, din in city[a[1]].items():
            new_din = din + a[0]
            if new_din < ans[des]:
                ans[des] = new_din
                heapq.heappush(queue, [new_din, des])

    return ans[end]




for _ in range(total_case):

    n, m, t = map(int, sys.stdin.readline().split())

    city = {}
    for k in range(1,n+1):
        city[k]={}

    s, g, h = map(int, sys.stdin.readline().split())

    for i in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        city[a][b] = d
        city[b][a] = d

    x_list = []

    for j in range(t):
        x = int(sys.stdin.readline())
        x_list.append(x)


    # start 에서 교차로 2개 경우의 수
    # 교차로 도착해서 목적지들 까지 경우의 수

    g_path = shortest(s,g) + shortest(g,h)# h부터 목적지들 구해서 short
    h_path = shortest(s,h) + shortest(h,g) # g부터 목적지들 구해서 short

    answer = []

    for path in x_list:
        new_path_g = g_path + shortest(h,path)
        new_path_h = h_path + shortest(g,path)

        tar = shortest(s,path)

        if (tar == new_path_g or tar == new_path_h) and tar != float('inf'):
            answer.append(path)

    answer.sort()

    print(' '.join(map(str, answer)))