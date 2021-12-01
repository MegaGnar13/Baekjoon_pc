#counter 이용
import collections
def solution(clothes):
    answer=[]
    for i in clothes:
        answer.append(i[1])
    a=collections.Counter(answer)
    b=list(a.values())
    count=1
    for i in b:
        count*=i+1
    return count-1
solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])


# 조합을 0부터 n개까지 만듬 -> 각 아이템마다 +1곱한거를 마지막에 -1하면 됨
# def solution(clothes):
#     answer = {}
#     for i in clothes:
#         if i[1] in answer:
#             answer[i[1]]+=1
#         else:
#             answer[i[1]]=1
#     list_a=list(answer.items())
#     print(list_a)
#     count=1
#     for i in list_a:
#         count*=i[1]+1
#     return count-1
# solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])


# itertools의 combination 이용하여 1개 뽑을 때부터 n개 뽑을 때까지 각각 구해서 더해줌 -> 시간초과
# import itertools
# def solution(clothes):
#     answer = {}
#     for i in clothes:
#         if i[1] in answer:
#             answer[i[1]]+=1
#         else:
#             answer[i[1]]=1
#     list_a=list(answer.items())
#
#     count=0
#     for i in range(1,len(list_a)+1):
#         a=itertools.combinations(list_a,i)
#         for j in a:
#             if len(j)==1:
#                 count+=j[0][1]
#             else:
#                 multi=1
#                 for k in range(len(j)):
#                     multi*=j[k][1]
#                 count+=multi
#     # print(count)
#     return count