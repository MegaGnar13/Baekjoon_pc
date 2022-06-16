import heapq
a = []

heapq.heappush(a, 4)
heapq.heappush(a, 3)
heapq.heappush(a, 2)
heapq.heappush(a, 1)

a.sort(reverse=True)

ans = heapq.heappop(a)
print(ans)

print(a)