
'''
 내 풀이
 end를 기준으로 +,- 1씩 시켜서 조건을 만족하는 값까지 찾기


 다른 사람 풀이
 나올 수 있는 모든 채널을 처음부터 끝까지 탐색 --> 탐색할 때마다 최소값 업데이트
'''
end = int(input())
bn = int(input())
bl = []
if bn>0:
    bl = list(map(int, input().split()))

start =100
ans = 0


num = list(map(int,set(str(end))))

if end == 100:
    print(0)

elif bn == 10:
    print(abs(end-start))
else:

    er = 0
    for _ in num:
        if _ in bl:
            er+=1

    if er == 0:
        print(min(len(str(end)), abs(end-100)))

    else:
        n1 = end - 1
        n2 = end + 1

        while end != start:

            if n1>=0:
                a1 = list(map(int,set(str(n1))))
                err1 = 0
                for i in a1:
                    if i in bl:
                        err1 += 1
                if err1 == 0:
                    ans = n1
                    break

            a2 = list(map(int,set(str(n2))))
            err2 = 0
            for j in a2:
                if j in bl:
                    err2+=1
            if err2 == 0:
                ans =n2
                break

            n1-=1
            n2+=1

        print(min(abs(end-100), len(str(ans))+abs(ans-end) ))


