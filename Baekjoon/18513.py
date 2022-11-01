from collections import deque
n, k = map(int, input().split())

lake = list(map(int, input().split()))

dx = [-1, 1]

m = {}

for i in lake:
    m[i+100000000] = 1

queue = deque([])

for i in lake:
    queue.append([i+100_000_000,0])

# print(queue)

ans = []

while len(ans) < k:
    next = queue.popleft()

    for i in range(2):
        nn = next[0] + dx[i]
        if nn not in m:
            m[nn] = 1
            queue.append([nn, next[1]+1])
            ans.append(next[1]+1)
            if len(ans) == k:
                break
#             # ans.append([nn, next[1]+1])
# print(lake)
# print(ans)
print(sum(ans))