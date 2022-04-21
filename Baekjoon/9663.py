a =int(input())
count_num = 0
answer = 0

chess = [[0 for i in range(a)] for j in range(a)]

def Queen(where): #where = [i,j]
    global chess_pan

    if count_num == A:
        return answer+1

    chess_pan[where[1]]=[1]*A
    for i in range(A):
        chess_pan[i][where[0]]=1


for i in range(a):
    for j in range(a):
        if chess[i][j] == 0:
            chess[i][j] = 1
            Queen()

        Queen([i,j])
print(answer)