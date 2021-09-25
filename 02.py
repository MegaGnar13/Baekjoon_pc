count_W = count_B =0
count_list = []
new = ['BBBWBWBW', 'BBBBWBWB', 'BBBWBWBW', 'BBBBWBWB', 'BBBWBWBW', 'BBBBWBWB', 'BBBWBWBW', 'BBBBWBWB']
for row in range(8):
    for columns in range(8):
        if (row + columns) % 2 == 0:
            if new[row][columns] == 'B':
                count_W += 1
            else:
                count_B += 1
        else:
            if new[row][columns] == 'W':
                count_W += 1
            else:
                count_B += 1
count_list.append(count_W)
count_list.append(count_B)
print((count_list))