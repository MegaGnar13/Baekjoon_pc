def solution(genres, plays):
    answer = {}
    for i in range(len(plays)):
        if genres[i] in answer:
            answer[genres[i]].append([i, plays[i]])
        else:
            answer[genres[i]] = [[i, plays[i]]]

    music = list(answer.items())
    for i in range(len(music)):
        music[i] = list(music[i])

    for i in range(len(music)):
        coco = 0
        for j in range(len(music[i][1])):
            coco += music[i][1][j][1]
        music[i].append(coco)

    music.sort(key=lambda x: -x[2])

    result = []
    for i in music:
        a = i[1]
        a.sort(key=lambda x: -x[1])
        if len(a) == 1:
            result.append(a[0][0])
        else:
            result.append(a[0][0])
            result.append(a[1][0])

    return result