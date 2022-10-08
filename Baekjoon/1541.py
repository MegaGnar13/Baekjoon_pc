import sys
a= sys.stdin.readline().rstrip()

tmp = a.split('-')

ttmp = []
for i in tmp:
    ttmp.append(list(map(int, i.split('+'))))

ans = 0
for i in range(len(ttmp)):
    if i == 0:
       ans += sum(ttmp[i])
    else:
        ans -= sum(ttmp[i])
print(ans)