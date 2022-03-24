a = 9
maxnum = 0
time = 0
ans = []
for i in range(a):
    b = int(input())
    time+=1
    if maxnum<b:
        maxnum = b
        ans = [b,time]
print(ans[0])
print(ans[1])