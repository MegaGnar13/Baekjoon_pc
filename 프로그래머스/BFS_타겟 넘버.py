def solution(numbers, target):
    if numbers == []:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return solution(numbers[1:], target+numbers[0]) + solution(numbers[1:], target-numbers[0])
print(solution([1,1,1,1,1],3))
#파이참에선 되는데 최종출력값이 안나온다해서 다시만들어야함

# util = ['p','m']
# util_result=[]
# list_a=[]
# answer=[]
# def solution(numbers,target):
#
#     if len(util_result)==len(numbers):
#
#         num=0
#
#         for i in range(len(numbers)):
#             if util_result[i]=='m':
#                 num-=numbers[i]
#             else:
#                 num+=numbers[i]
#         if num == target:
#             answer.append(1)
#         if util_result == ['m']*len(numbers):
#             a=len(answer)
#             return(a)
#         return
#
#     for j in range(len(util)):
#         util_result.append(util[j])
#         solution(numbers,target)
#         util_result.pop()
#
#     return len(answer)
# solution([1,1,1,1,1],3)

# def soltion(numbers, target):
#     answer = list_a.count(target)
#     print(answer)
#     return answer
# soltion([1,1,1,1,1],3)