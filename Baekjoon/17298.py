#오큰수
import sys
import collections
A=int(sys.stdin.readline())
B=list(map(int,sys.stdin.readline().split()))

C=collections.deque(B)
answer=[-1]*A
stack=[]
# out=[]
while len(C)!=0:

    a=C.popleft()

    if len(stack) > 0:
        while True:
            if len(stack)==0:
                break
            if stack[-1][0]<a:
                n=stack.pop()
                n[1]=a
                # out.append(n)
                answer[n[2]]=n[1]
            else:
                break
    stack.append([a, -1, B.index(a)])
print(*answer)
# print(stack)
# print(out)
# answer=out+stack
# answer.sort(key=lambda x:x[2])
# for i in answer:
#     print(i[1],end=' ')

#시간초과
# import sys
# A=int(sys.stdin.readline())
# B=list(map(int,sys.stdin.readline().split()))
# answer=[]
# for i in range(len(B)):
#     new_list=[]
#     for j in range(i+1,len(B)):
#         if B[j]>B[i]:
#             new_list.append(B[j])
#             continue
#     if len(new_list) ==0:
#         new_list.append(-1)
#     answer.append(new_list[0])
# print(*answer)
# for i in answer:
    # print(i,end=' ')