sec_num = int(input())

prime_list = [2]
i=2
ans=[]
while sec_num != 1:
    if sec_num % i == 0:
        ans.append(i)
        sec_num = sec_num//i
    else:
        i+=1

for i in ans:
    print(i)