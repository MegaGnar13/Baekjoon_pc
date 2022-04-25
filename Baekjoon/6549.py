import sys

while True:
    n = list(map(int, sys.stdin.readline().split()))
    aans = 0

    if n[0] == 0:
        break

    num = n[0]

    n = n[1:]


    stack = []

    for i,j in enumerate(n):
        # print(stack)
        if not stack:
            stack.append([i,j])

        else:
            if j > stack[-1][1]:
                stack.append([i,j])

            elif j == stack[-1][1]:
                continue

            else:
                tem_i = 0

                while True:
                    if not stack:
                        stack.append([tem_i,j])
                        break

                    a = stack.pop()

                    if j < a[1]:
                        tem_i = a[0]

                        tar = (i-a[0]) * a[1]
                        if aans < tar:
                            aans = tar

                    else:
                        if j == a[1]:
                            # print('same',a)
                            stack.append(a)
                            break
                        else:
                            stack.append(a)
                            stack.append([tem_i,j])
                            # print('big',a)
                            break

    for i in stack:

        if (num-i[0]) * i[1] > aans:
            aans = (num-i[0]) * i[1]

    print(aans)