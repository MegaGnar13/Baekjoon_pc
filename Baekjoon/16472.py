l = int(input())
alpha = input()

first = 0
second = 1

ans = 0

temp = {}
if alpha[0] == alpha[1]:
    temp[alpha[0]] = 2
else:
    temp[alpha[0]] = 1
    temp[alpha[1]] = 1

while True:

    if len(temp) <= l:
        ans = max(ans, second-first+1)
        second += 1

        if second == len(alpha):
            break


        if alpha[second] not in temp:
            temp[alpha[second]] = 1
        else:
            temp[alpha[second]] += 1

    elif len(temp) > l:

        temp[alpha[first]] -= 1

        if temp[alpha[first]] == 0:
            temp.pop(alpha[first])

        first += 1

print(ans)