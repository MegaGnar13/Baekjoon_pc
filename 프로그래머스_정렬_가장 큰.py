def solution(numbers):
    str_list=[]
    for index,num in enumerate(numbers):
        if num<10:
            num=num*1111
        elif num<100:
            num=num*101
        elif num<1000:
            num=num*10+(num//100)
        str_list.append([num,index])

    str_list.sort(reverse=True)
    answer=[]
    for i in range(len(numbers)):
        annum=str(numbers[str_list[i][1]])
        answer.append(annum)
    last=''.join(answer)
    num=int(last)
    return str(num)


# 시간복잡도가 O(n**n) 시간초과 됨
import itertools
# def solution(numbers):
#     iterable = numbers
#     result=itertools.permutations(iterable)
#     num_list=[]
#     for i in result:
#
#         b=[str(num) for num in i]
#         c=''.join(b)
#         num_list.append(int(c))
#     print(max(num_list))
#     return str((max(num_list)))

# 람다 사용
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))