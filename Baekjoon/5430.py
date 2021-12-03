import collections

num = int(input())
for i in range(num):
    case = input()
    list_case = list(case)
    num_cnt = int(input())
    list_num = input()

    del_char = ["[", "]"]

    for i in range(len(del_char)):
        list_num = list_num.replace(del_char[i], "")

    list_num_int = list_num.split(",")

    cnt_D = list_case.count("D")
    cnt_R = 0
    if cnt_D > len(list_num_int) or list_num_int == ['']:
        print("error")
        continue

    list_num_int = collections.deque(list_num_int)

    for j in list_case:
        if j == "R":
            cnt_R += 1
        elif j == "D":
            if cnt_R % 2 == 0:
                list_num_int.popleft()
            else:
                list_num_int.pop()

    if cnt_R % 2 == 0:
        print("["+",".join(list_num_int)+"]")
    else:
        list_num_int.reverse()
        print("[" + ",".join(list_num_int) + "]")

import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
