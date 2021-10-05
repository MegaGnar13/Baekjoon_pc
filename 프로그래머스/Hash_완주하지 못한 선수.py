import collections

def solution(participant, completion):
    answer_1 = collections.Counter(participant)-collections.Counter(completion)

    return (list(answer_1.keys())[0])
print(solution(["leo", "kiki","eden"],["eden", "kiki"]))