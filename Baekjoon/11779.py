import heapq
import sys
city = int(sys.stdin.readline())
bus = int(sys.stdin.readline())

ci = {}
for i in range(1, city+1):
    ci[i] = {}

for i in range(bus):
    start, end, weight = map(int, sys.stdin.readline().split())

    if end in ci[start]:
        if weight < ci[start][end]:
            ci[start][end] = weight
    else:
        ci[start][end] = weight

start_city, end_city = map(int, sys.stdin.readline().split())

# print(ci)

def dijstra(start_city):
    queue = [[0, start_city, [start_city]]]
    ans = [1e9 for i in range(city+1)]

    while queue:
        # print(queue)

        a = heapq.heappop(queue)

        if a[1] == end_city:
            return a[0],a[2]

        if a[0] < ans[a[1]]:
            ans[a[1]] = a[0]

            tar = a[2].copy()
            target = a[2].copy()

            for k in ci[a[1]]:

                new_des = k
                new_dis = a[0] + ci[a[1]][k]

                if new_dis < ans[new_des]:

                    tar.append(new_des)
                    # print(tar)
                    heapq.heappush(queue, [new_dis, new_des, tar])
                    tar = target.copy()

answer = dijstra(start_city)

# print(answer)
print(answer[0])
print(len(answer[1]))
print(*answer[1])