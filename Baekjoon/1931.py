A=int(input())
B=[list(map(int,input().split())) for i in range(A)]
# B.sort()
time_list=[]

C=sorted(B,key=lambda x:(x[1],x[0]))
time_list.append(C[0])

for i in range(1,len(C)):
    if C[i][0]>=time_list[-1][1]:
        time_list.append(C[i])

print(len(time_list))

