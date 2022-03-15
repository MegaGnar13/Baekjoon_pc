def prime_num(num):
    pan = [True]*num
    m = int(num**(0.5))
    for i in range(2, m+1):
        if pan[i] == True:
            for j in range(i+i, num, i):
                pan[j] = False

    return [i for i in range(2,num) if pan[i] == True]

i = int(input())
pr = prime_num(10000)
for _ in range(i):
    ans = []
    num = int(input())
    A = num // 2
    B = A
    while True:

        if A in pr and B in pr:
            print(A, B)
            break
        else:
            A-=1
            B+=1


