import sys
from collections import deque
A=list(map(int,sys.stdin.readline().split()))
deq= deque()
for i in range(A[0]):
    deq.append(i)
answer_list=[]
while len(deq)>=A[1]:
    answer_list.append(deq[A[1]-1]+1)
    deq.rotate(-(A[1]-1))
    deq.popleft()
while len(deq)>0:
    deq.rotate(-(A[1]%len(deq)-1))
    answer_list.append(deq[0]+1)
    deq.popleft()

print('<',end='')
print(*answer_list,sep=', ',end='')
print('>')