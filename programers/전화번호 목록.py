#길이가 아니라 그냥 sort하면 다음 값하고만 비교하면 됨
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):

        first=hash(phone_book[i])
        bigo=phone_book[i+1]
        bigo_1=bigo[0:len(phone_book[i])]
        second=hash(bigo_1)

        if first==second:
            return False
        else:
            continue
    answer = True
    return answer
# #비교하고자 하는 접두사를 hash로 만듬
# def solution(phone_book):
#     phone_book.sort(key=lambda x:len(x))
#
#     for i in range(len(phone_book)-1):
#
#         first=hash(phone_book[i])
#
#         for j in range(i+1,len(phone_book)):
#             bigo=phone_book[j]
#             bigo_1=bigo[0:len(phone_book[i])]
#             second=hash(bigo_1)
#
#             if first==second:
#                 return False
#             else:
#                 continue
#     answer = True
#     return answer
# 앞에서부터 한 원소씩 비교
# def solution(phone_book):
#     phone_book.sort(key=lambda x:len(x))
#
#     for i in range(len(phone_book)-1):
#         for j in range(i+1,len(phone_book)):
#             count=0
#             for k in range(len(phone_book[i])):
#                 if phone_book[i][k] == phone_book[j][k]:
#                     count+=1
#                 else:
#                     break
#             if count==len(phone_book[i]):
#                 return False
#     answer = True
#     return answer