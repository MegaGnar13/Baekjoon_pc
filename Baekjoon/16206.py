import heapq
N, M = map(int, input().split())

l = list(map(int, input().split()))

ans = 0
temp = []
ten = []

for i in range(len(l)):
    if l[i] == 10:
        ans += 1
    elif l[i] > 10:
        if l[i] % 10 == 0:
            heapq.heappush(ten,l[i])
        else:
            heapq.heappush(temp, l[i])

for _ in range(M):

    if ten:
        a = heapq.heappop(ten)

        ans += 1

        if a - 10 == 10:
            ans += 1

        elif a - 10 > 10:
            if (a - 10) % 10 == 0:
                heapq.heappush(ten, a-10)
            else:
                heapq.heappush(temp, a - 10)


    elif temp:
        a = heapq.heappop(temp)

        ans += 1

        if a - 10 == 10:
            ans += 1

        elif a - 10 > 10:
            if (a - 10) % 10 == 0:
                heapq.heappush(ten, a - 10)
            else:
                heapq.heappush(temp, a - 10)

print(ans)