n = int(input())

ans = 0
ans_list = list()

for i in range(n//2, n+1):
    cnt = 0
    cnt_list = [n]

    n_tar = n
    tar = i


    while True:

        next = n_tar - tar
        if next >= 0:
            cnt_list.append(tar)

            n_tar = tar
            tar = next

            cnt += 1
        else:
            cnt_list.append(tar)
            break

    if ans < cnt:
        ans = cnt
        ans_list = cnt_list

print(ans+2)
print(*ans_list)
