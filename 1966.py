from collections import deque
A=int(input())
for i in range(A):
    B=list(map(int,input().split()))
    C=deque(list(map(int,input().split())))

    num = C[B[1]]
    count=0
    C[B[1]]=0 # 중복되면 index 찾기 어려우니 범위 밖인 0으로 바꿔줌

    #원하는 값 보다 높은 수들 먼저 나가게

    while num < max(C):
        C.rotate(-(C.index(max(C))))
        C.popleft()
        count+=1

    #원하는 값이 왔을 때 중복일 수도 있으니 순서대로 count
    for i in range(C.index(0)):
        if C[i] == num:
            count+=1

    print(count+1)