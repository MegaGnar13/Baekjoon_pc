# 초기화 할 필요 없음
a = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]


def cal(num):
    length = len(zero)
    if length <= num:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print("%d %d" % (zero[num], one[num]))


for i in range(a):
    k = int(input())
    cal(k)

#출처: https: // doorbw.tistory.com / 58[Tigercow.Door]

# one, zero 값 초기화 시켜야 함
# A = int(input())
#
# zero = [1,0]
# one = [0,1]
# def fibo(num):
#     if num == 0:
#         return zero[0], one[0]
#     if num == 1:
#         return zero[1], one[1]
#
#
#     for i in range(2,num+1):
#         zero.append(zero[i-1]+zero[i-2])
#         one.append(one[i-1]+one[i-2])
#
#     return zero[num],one[num]
#
#
#
# answer= []
# for i in range(A):
#     B = int(input())
#     a=fibo(B)
#     answer.append(a)
#     zero = [1, 0]
#     one = [0, 1]
#
# for i in answer:
#     print(i[0],i[1])






# 시간초과 나옴
#
# num_list=[]
# for i in range(A):
#     B= int(input())
#     num_list.append(B)
# num_0 = []
# num_1 = []
# def fibo(n):
#
#     if n == 0:
#         num_0.append(1)
#         return 1
#     if n == 1:
#         num_1.append(1)
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
#
#
# for i in num_list:
#     fibo(i)
#
#     print(sum(num_0),sum(num_1))
#     num_0=[]
#     num_1=[]

