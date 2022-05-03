tar = list(input())
b = list(input())
ans = []

for i in range(len(tar)):
    if tar[i] != b[-1]:
        ans.append(tar[i])

    else:
        ans.append(tar[i])

        if len(ans) >= len(b):
            t = -1
            while ans:
                # print(ans)

                if ans[t] == b[t]:
                    # print(t)
                    if t == -len(b):
                        for i in range(len(b)):

                            ans.pop()
                        break
                    else:
                        t -= 1
                else:
                    break
ans = ''.join(ans)

if ans == '':
    print("FRULA")
else:
    print(''.join(ans))