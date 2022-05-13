from collections import deque
m = [0 for i in range(100001)]
ti = [0 for j in range(100001)]
li = {}


n, k = map(int, input().split())

an_time = 0

queue = deque([[n, 0]])

m[n] = 1
li[n]=[n]

if k < n:

    print(n-k)
    for i in range(n,k-1,-1):
        print(i,end=" ")

else:


    while queue:
        location, time = queue.popleft()

        if location == k:
            print(time)
            print(*li[location])
            break

        first = location - 1
        second = location + 1
        third = location * 2

        if first >= 0 and m[first] == 0:
            m[first] = 1
            queue.append([first, time + 1])
            li[first] = []
            li[first].extend(li[location])
            li[first].append(first)

        if second <= 100000 and m[second] == 0:
            m[second] = 1
            queue.append([second, time + 1])
            li[second] = []
            li[second].extend(li[location])
            li[second].append(second)

        if third <= 100000 and m[third] == 0:
            m[third] = 1
            queue.append([third, time + 1])
            li[third] = []
            li[third].extend(li[location])
            li[third].append(third)

        del li[location]
