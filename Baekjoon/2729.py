import sys
'''
 내 풀이방법 
 이진수를 int로 더하고 뒤에서부터  2면 10으로 바꾸고 3이면 11로 바꿈
 맨 앞은 범위 밖이기 때문에 따로 조건을 통해 2나3이면 새로 1을 append

'''

#
# a = int(input())
# from collections import deque
#
# for i in range(a):
#     x,y = map(int,input().split())
#
#     ans = x+y
#     # print(ans)
#     ans = deque(list(map(int,str(ans))))
#     # print(ans)
#     for j in range(len(ans)):
#         tar = -(j+1)
#         if ans[tar] == 0 or ans[tar] == 1:
#             continue
#         elif ans[tar] == 2:
#             if j == len(ans)-1:
#                 ans[tar] = 0
#                 ans.appendleft(1)
#             else:
#                 ans[tar] = 0
#                 ans[tar-1] += 1
#         elif ans[tar] ==3:
#             if j == len(ans)-1:
#                 ans[tar] = 1
#                 ans.appendleft(1)
#             else:
#                 ans[tar] = 1
#                 ans[tar-1] += 1
#     print(''.join(map(str,ans)))


'''
다른 풀이
2진수들을 10진수로 바꾸고 더한다음에 다시 2진수로 바꿈
int(num, 2)  --> 2진수의 num을 10진수로 바꿈
bin(num)   --> 10진수의 num을 2진술 바꿈 (이때 str type으로 변환)
'''

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a,b = input().split(" ")
    a = int(a,2)
    b = int(b,2)

    c = bin(a + b)
    print(type(a))
    print(type(c))
    print(bin(a+b))
    print(bin(a + b).replace("0b", ""))

