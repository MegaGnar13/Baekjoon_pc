import sys
sys.setrecursionlimit(10**9)
num = int(input())

inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

position = [0]*(num+1)
for i in range(num):
    position[inorder[i]] = i

# print(position)

def post(in_first, in_end, post_first, post_end):
    if in_first > in_end or post_first > post_end:
        return

    parent = postorder[post_end]
    tar = position[parent]

    left = tar - in_first
    right = in_end - tar

    print(postorder[post_end], end = ' ')

    post(in_first, in_first + left - 1, post_first, post_first + left - 1)
    post(in_end - right + 1, in_end, post_end - right , post_end - 1)


post(0, num-1, 0, num-1)