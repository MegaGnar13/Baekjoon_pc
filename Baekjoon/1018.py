A, B = map(int,input().split())

chess_pan = []
for low in range(A):
    C= input()
    chess_pan.append(C)

new_chess_pan =[]
for i in range(A-7):
    for j in range(B-7):
        new_chess_pan.append(list((row[j:j+8] for row in chess_pan[i:i+8])))

count_list =[]


for new in new_chess_pan:

    count_W = 0
    count_B = 0
    for row in range(8):
        for columns in range(8):
            if (row+columns)%2 == 0:
                if new[row][columns] == 'B':
                    count_W+=1
                else:
                    count_B+=1
            else:
                if new[row][columns] == 'W':
                    count_W += 1
                else:
                    count_B += 1
    count_list.append(count_W)
    count_list.append(count_B)

print(min(count_list))

"""
처음부터 판을 옮기는게 아니라 일정 범위를 나누어서 바로 확인
"""

y, x = map(int, input().split())

chess = []
for _ in range(y):
    a = input()
    chess.append(a)

#처음이 W일 때
cntt = []
for n in range(y-7):
    for m in range(x - 7):
        cnt_W = 0
        for i in range(n,8+n):
            for j in range(m,m+8):
                if (i+j)%2 == 0 and chess[i][j]=='B':
                    cnt_W += 1
                elif (i+j)%2 == 1 and chess[i][j] == 'W':
                    cnt_W += 1
        cntt.append(cnt_W)

#처음이 B일 때
for n in range(y - 7):
    for m in range(x - 7):
        cnt_B = 0
        for i in range(n, 8 + n):
            for j in range(m, m + 8):
                if (i + j) % 2 == 0 and chess[i][j] == 'W':
                    cnt_B += 1
                elif (i + j) % 2 == 1 and chess[i][j] == 'B':
                    cnt_B += 1
        cntt.append(cnt_B)


print(min(cntt))