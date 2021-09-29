#다음에 시간 나면 greedy algo로 풀어보기

#dynamic algo
def num(N):
    if N == 1:
        a=[1,1,1,1,1,1,1,1,1,1]
        return a
    else:
        b=[0,0,0,0,0,0,0,0,0,0]

        a=num(N-1)
        for i in range(len(a)):
            if i == 0:
                b[i]=a[i+1]
            elif i == len(a)-1:
                b[i]=a[i-1]
            else:
                b[i]=a[i-1]+a[i+1]
        a=b

    return a
A=int(input())
answer=sum(num(A))-num(A)[0]
print(answer%1000000000)