A=int(input())
B=[list(map(int,input().split())) for _ in range(A)]
count_0 = 0
count_1 = 0
def square_1(square):
    global  count_0,count_1
    if len(square)==1:
        if square[0][0] == 0:
            count_0 +=1
        elif square[0][0] == 1:
            count_1 +=1
        return count_0,count_1

    square_num = 0
    for i in square:
        for j in i:
            square_num += j
    if square_num == 0:
        count_0 += 1
    elif square_num == len(square) ** 2:
        count_1 += 1
    else:
        square_A=[square[i][0:len(square)//2] for i in range(0,len(square)//2)]
        square_B=[square[i][len(square)//2:len(square)] for i in range(0,len(square)//2)]
        square_C=[square[i][0:len(square)//2] for i in range(len(square)//2,len(square))]
        square_D=[square[i][len(square)//2:len(square)] for i in range(len(square)//2,len(square))]

        square_1(square_A)
        square_1(square_B)
        square_1(square_C)
        square_1(square_D)

    return count_0,count_1
a,b=square_1(B)
print(a)
print(b)