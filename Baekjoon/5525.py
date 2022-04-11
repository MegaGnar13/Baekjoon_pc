import sys
num = int(input())

length = int(input())

target = sys.stdin.readline().rstrip()

ans = 0
i=0
count = 0
while i<length-2:

    if target[i] == "I" and target[i+1] == "O" and target[i+2] == "I":
        count +=1
        i+=2
        if num == count:
            # print(i)
            count -= 1
            ans += 1

    else:
        i+=1
        count = 0

print(ans)