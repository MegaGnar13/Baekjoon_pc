from sys import stdin

N = int(stdin.readline())
villages = []
people=0
for _ in range(N):
    pos, peo = map(int, stdin.readline().split())
    villages.append((pos, peo))
    people += peo
villages.sort(key=lambda x : x[0])

count = 0
tar = 0
for pos, peo in villages:
    count+=peo
    if count>(people/2):
        tar = pos
        break

ans1 = 0
ans2 = 0
for i in range(len(villages)):
    ans1 += abs(tar-villages[i][0]) * villages[i][1]
    ans2 += abs(tar-1-villages[i][0]) * villages[i][1]

if ans2 <= ans1:
    print(tar-1)
else:
    print(tar)