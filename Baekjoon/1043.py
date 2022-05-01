import sys
n, m = map(int, sys.stdin.readline().split())

real = list(map(int, sys.stdin.readline().split()))

real_peaple = real[0]
real_list = real[1:]

party = []

for i in range(m):
    party.append(list(map(int, sys.stdin.readline().split()))[1:])


# print(real_list)
# print(party)

zinsil = [0 for i in range(n+1)]

for _ in range(real_peaple):
    zinsil[real_list[_]] = 1

while real_list:
    i = real_list.pop()
    for j in range(len(party)):
        if i in party[j]:
            # print("remove")
            for kk in party[j]:
                if zinsil[kk] == 0:
                    real_list.append(kk)
                    zinsil[kk] = 1

            party[j] = [0]

ans = 0
for aa in party:
    if aa != [0]:
        ans += 1

print(ans)