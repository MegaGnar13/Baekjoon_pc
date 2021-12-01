import itertools
A = int(input())
list_A= []
for i in range(A):
    B=list(map(int,input().split()))
    list_A.append(B)

mem_list=[]
score_list=[]
for i in range(A):
    mem_list.append(i)
result = itertools.combinations(mem_list,A//2)

for i in result:
    clone=[i for i in range(A)]
    for j in i:
        clone.remove(j)
    score_AA = 0
    for AA in range(A//2):
        for BB in range(A//2):
            if AA!=BB:
                score_AA+=list_A[i[AA]][i[BB]]
    score_BB = 0
    for AA in range(A//2):
        for BB in range(A//2):
            if AA!=BB:
                score_BB+=list_A[clone[AA]][clone[BB]]
    #노가다의 흔적.. 처음에 3명으로 생각했을 때 짠 것
    # score_A=list_A[i[0]][i[1]]+list_A[i[1]][i[0]]+list_A[i[0]][i[2]]+list_A[i[2]][i[0]]+list_A[i[1]][i[2]]+list_A[i[2]][i[1]]
    # score_B=list_A[clone[0]][clone[1]]+list_A[clone[1]][clone[0]]+list_A[clone[0]][clone[2]]+list_A[clone[2]][clone[0]]+list_A[clone[1]][clone[2]]+list_A[clone[2]][clone[1]]
    score=score_AA-score_BB
    if score>=0:
        score_list.append(score)

print(min(score_list))

# 처음에 무조건 2명씩 팀 짜는건줄 ㅠㅠ
# import itertools
# A = int(input())
# list_A= []
# for i in range(A):
#     B=list(map(int,input().split()))
#     list_A.append(B)
# print(list_A)
# mem_list=[]
# score_list=[]
# for i in range(A):
#     mem_list.append(i)
# result = itertools.combinations(mem_list,2)
#
# for i in result:
#     clone=[i for i in range(A)]
#     for j in i:
#
#         clone.remove(j)
#     result_2 = itertools.combinations(clone,2)
#     for k in result_2:
#
#         score=list_A[i[0]][i[1]]+list_A[i[1]][i[0]]-list_A[k[0]][k[1]]-list_A[k[1]][k[0]]
#         score_list.append(score)
#         print([i,k,score])
#
#
#
# answer = []
#
# for i in score_list:
#     if i>=0:
#         answer.append(i)
# print(min(answer))
