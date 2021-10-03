#오큰수
import sys
A=int(sys.stdin.readline())
B=list(map(int,sys.stdin.readline().split()))
answer=[]
for i in range(len(B)):
    new_list=[]
    for j in range(i+1,len(B)):
        if B[j]>B[i]:
            new_list.append(B[j])
            continue
    if len(new_list) ==0:
        new_list.append(-1)
    answer.append(new_list[0])
print(*answer)
# for i in answer:
    # print(i,end=' ')