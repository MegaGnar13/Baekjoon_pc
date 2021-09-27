A =int(input())
count_num = 0
answer = 0
def Queen(where): #where = [i,j]
    global chess_pan

    if count_num == A:
        return answer+1

    chess_pan[where[1]]=[1]*A
    for i in range(A):
        chess_pan[i][where[0]]=1

#다 차있을 때 끝내는 방법
    # a=0
    # for i in chess_pan:
    #     a+=sum(i)
    #     if a==A**2:
    #         print(1)
    #         return

    print(chess_pan)
    for i in range(A):
        for j in range(A):
            if chess_pan[i][j] == 0:
                a=[i,j]
                Queen(a)


for i in range(A):
    for j in range(A):
        chess_pan = [[0 for i in range(1, A + 1)] for i in range(1, A + 1)]
        Queen([i,j])
print(answer)