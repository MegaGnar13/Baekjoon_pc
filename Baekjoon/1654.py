import sys
sys.setrecursionlimit(10**6)
A, B=map(int,sys.stdin.readline().split())
lines=[int(sys.stdin.readline()) for i in range(A)]
start=1
end=max(lines)
result=0
while start<=end:
    mid=(start+end)//2
    cnt=0
    for i in lines:
        cnt+=i//mid
    if cnt>=B:
        result=mid
        start=mid+1
    else:
        end=mid-1
print(result)

#  왜 reculsive error가 뜰까.
# def solution(start,end,target):
#     mid=(start+end)//2
#     cnt=0
#     for i in lines:
#         cnt+=i//mid
#     if cnt<target:
#         end=mid-1
#         return solution(start,end,target)
#     elif cnt>target:
#         start=mid+1
#         return solution(start,end,target)
#     else:
#         return mid
#
# start=1
# end=max(lines)
# a=(solution(start,end,B))
#
# while True:
#     cnt=0
#     for i in lines:
#         cnt+=i//a
#     if cnt==B:
#         a+=1
#     elif cnt<B:
#         break
# print(a-1)