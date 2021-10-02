def solution(progresses, speeds):
    answer = []
    while len(progresses)>=1:
        while progresses[0]<100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

        answer_1 = []
        while True:
            for i in range(len(progresses)):
                if progresses[0] >= 100:
                    answer_1.append(progresses[0])
                    progresses.pop(0)
                    speeds.pop(0)
                else:
                    break
            break

        answer.append(len(answer_1))

    return answer

solution([93,30,55],[1,30,5])
# print(solution([93,30,55],[1,30,5]))