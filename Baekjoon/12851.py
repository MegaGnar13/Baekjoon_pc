from collections import deque
m = [0 for i in range(100001)]
ti = [0 for j in range(100001)]

n, k = map(int, input().split())

an_time = 0

queue = deque([[n, 0]])

ti[n] = 1


while queue:
    a = queue.popleft()
    # print(a)


    if a[1] > an_time and an_time!=0:
        break

    first = a[0]-1
    second = a[0]+1
    third = 2*a[0]



    if first == k:
        if an_time == 0:
            an_time = a[1]+1

            ti[first] += ti[a[0]]
        else:

            if a[1]+1 == an_time:
                ti[first] += ti[a[0]]

            else:
                break

    else:
        if first >= 0:
            if m[first] == 0:
                queue.append([first, a[1]+1])
                ti[first] += ti[a[0]]
                m[first] = a[1] + 1

            elif m[first] == a[1] + 1:
                ti[first] += ti[a[0]]



    if second == k:
        if an_time == 0:
            an_time = a[1]+1

            ti[second] += ti[a[0]]
        else:

            if a[1]+1 == an_time:
                ti[second] += ti[a[0]]

            else:
                break

    else:
        if second <= 100000:
            if m[second] == 0:
                queue.append([second, a[1]+1])
                ti[second] += ti[a[0]]
                m[second] = a[1] + 1

            elif m[second] == a[1] + 1:
                ti[second] += ti[a[0]]


    if third == k:
        if an_time == 0:
            an_time = a[1]+1

            ti[third] += ti[a[0]]
        else:

            if a[1]+1 == an_time:
                ti[third] += ti[a[0]]

            else:
                break

    else:
        if third <= 100000:
            if m[third] == 0:
                queue.append([third, a[1]+1])
                ti[third] += ti[a[0]]
                m[third] = a[1] + 1

            elif m[third] == a[1] + 1:
                ti[third] += ti[a[0]]

if n == k:
    print(0)
    print(1)
else:

    print(an_time)
    # print(method)
    print(ti[k])