import collections

def solution(prices):
    answer = []
    result = []
    prices = collections.deque(prices)
    count  = [0]*len(prices)
    idx=0
    while len(prices) > 0:
        idx+=1
        a = prices.popleft()
        # print(a)
        # print(answer)
        if len(answer) == 0:
            answer.append([a,0,idx])
        else:
            for i in answer:
                i[1] += 1

            while answer[-1][0] > a:
                b = answer.pop()
                result.append(b)
                if len(answer)==0:
                    answer.append([a,0,idx])
                    break

            answer.append([a, 0,idx])

    for i in answer:
        count[i[2]-1]=i[1]
    for i in result:
        count[i[2]-1]=i[1]
    # print(count)
    return count