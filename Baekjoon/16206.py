import heapq
N, M = map(int, input().split())

l = list(map(int, input().split()))

ans = 0
temp = []
for i in range(len(l)):
    if l[i] == 10:
        ans += 1
    elif l[i] > 10:
        heapq.heappush(temp, l[i])
temp.sort(reverse = True)

for _ in range(M):

    if temp:
        a = heapq.heappop(temp)

        ans += 1

        if a - 10 == 10:
            ans += 1

        elif a - 10 > 10:
            heapq.heappush(temp, a-10)

print(ans)