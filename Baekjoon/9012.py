A=int(input())
B=[list(input()) for i in range(A)]
def blacket(list):
    count_num=0
    for i in list:
        if i == '(':
            count_num+=1
        if i == ')':
            if count_num==0:
                return 'NO'
            else:
                count_num-=1
    if count_num ==0:
        return 'YES'
    else:
        return 'NO'
for i in B:
    print(blacket(i))