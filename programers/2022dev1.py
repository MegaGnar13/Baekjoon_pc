def solution(grade):

    answer = 0
    temp = grade[-1]
    for i in reversed(grade):
        if i > temp:
            answer += (i - temp)
        else:
            temp = i

    return answer