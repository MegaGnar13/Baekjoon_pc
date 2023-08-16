while True:
    a = int(input())
    if a == -1:
        break

    d = []

    start = 1

    for i in range(start,a):
        if a % i == 0:
            d.append(i)

    if sum(d) == a:
        tmp = ''
        for i in d:
            if d.index(i) == len(d) -1:
                tmp += str(i)
                break
            tmp += str(i)+ ' + '


        print(a, '=', tmp)
    else:
        print(a, 'is NOT perfect.')