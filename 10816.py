import collections
from sys import stdin
A = stdin.readline()
B = sorted(map(int,stdin.readline().split()))
C = stdin.readline()
D = map(int,stdin.readline().split())

answer=[]
a=collections.Counter(B)
# print(a)
for i in D:
    if i in a:
        answer.append(a[i])
    else:
        answer.append(0)

print(*answer)
# end_point=len(B)
# # print(B)
# answer=[]
# def cntnum(item,n,start,end,count):
#     mid=(start+end)//2
#     # print([start,mid,end])
#     if item[mid]==n:
#         count+=1
#         start=mid-1
#         end=mid+1
#
#         if start>=0:
#             while item[start]==n:
#                 count+=1
#                 if start ==0:
#                     break
#                 start-=1
#
#         if end <= len(item) - 1:
#             while item[end]==n:
#                 count+=1
#                 if end == len(item)-1:
#                     break
#                 end+=1
#         answer.append(count)
#         return
#
#     if item[mid] != n:
#         if start==end or start>mid or end<mid or start>end:
#             answer.append(0)
#             return
#
#         elif item[mid]>n:
#             end=mid-1
#             cntnum(item,n,start,end,count)
#         else:
#             start=mid+1
#             cntnum(item, n, start, end, count)
#
#     return
#
# for i in D:
#     cntnum(B,i,0,end_point-1,0)
# print(*answer)