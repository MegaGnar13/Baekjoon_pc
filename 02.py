A=int(input())
cnt=0
count=0
while True:
    if cnt>=A:
        break
    count+=1
    cnt+=count

a=(A-(cnt-count))
if count%2==0:
    print(a,'/',count+1-a,sep='')
else:
    print(count + 1 - a, '/',a , sep='')