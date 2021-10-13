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
    print(music[1][2])

    music.sort(key=lambda x: -x[2])
    print(music)

    return answer
solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])