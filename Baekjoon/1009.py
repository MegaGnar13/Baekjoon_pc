num = int(input())

for i in range(num):

    a, b = map(int,input().split())

    ans = (a**b) %10

    print(ans)