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

