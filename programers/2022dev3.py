from collections import deque

def solution(rows, columns, lands):
    answer = []
    lake = [[0 for i in range(columns)] for j in range(rows)]

    for i in lands:
        lake[i[0]-1][i[1]-1] = 1

    def bfs(s_y, s_x):

        lake[s_y][s_x] = 2

        queue = deque([[s_y, s_x]])

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        temp = 0

        while queue:

            a = queue.popleft()
            temp += 1

            for i in range(4):
                nx = a[1] + dx[i]
                ny = a[0] + dy[i]

                if 0 <= nx <= columns - 1 and 0 <= ny <= rows - 1:
                    if lake[ny][nx] == 0:
                        lake[ny][nx] = 2
                        queue.append([ny, nx])
        # print(temp)
        return temp

    bfs(0, 0)

    min_an = 10e9
    max_an = 0

    for i in range(rows):
        for j in range(columns):
            if lake[i][j] == 0:
                tar = bfs(i,j)

                min_an = min(min_an, tar)
                max_an = max(max_an, tar)


    if min_an == 10e9:
        answer.append(-1)
    else:
        answer.append(min_an)

    if max_an == 0:
        answer.append(-1)
    else:
        answer.append(max_an)

    # print(answer)
    return answer
