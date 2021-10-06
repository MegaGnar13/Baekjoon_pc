import sys
import heapq
A=int(sys.stdin.readline())
jung_left=[]
jung_right=[]


B=[int(sys.stdin.readline()) for i in range(A)]
jung=B[0]
print(B.pop(0))
for i in B:

    if i<jung:
        heapq.heappush(jung_left,(-i,i))
    else:
        heapq.heappush(jung_right,i)

    if len(jung_left)-len(jung_right)>=2:
        heapq.heappush(jung_right,jung)
        jung=heapq.heappop(jung_left)[1]
    elif len(jung_right)-len(jung_left)>=2:
        heapq.heappush(jung_left,(-jung,jung))
        jung=heapq.heappop(jung_right)

    if len(jung_left)>0 and (len(jung_left)+len(jung_right))%2==1 and len(jung_left)>len(jung_right):
        if jung_left[0][1]<jung:
            heapq.heappush(jung_right,jung)
            jung=heapq.heappop(jung_left)[1]
    print(jung)
