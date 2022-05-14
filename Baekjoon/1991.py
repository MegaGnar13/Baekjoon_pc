num = int(input())

tree = {}

first = ''
for i in range(num):
    a, b, c = input().split()
    if i == 0:
        first = a

    tree[a] = [b, c]

# print(tree)

pre= []
def preorder(tar):

    pre.append(tar)

    left = tree[tar][0]
    right = tree[tar][1]

    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)

preorder(first)
print(''.join(pre))

ino = []
def inorder(tar):

    left = tree[tar][0]
    right = tree[tar][1]

    if left != '.':
        inorder(left)

    ino.append(tar)

    if right != '.':
        inorder(right)

inorder(first)
print(''.join(ino))

post = []
def postorder(tar):

    left = tree[tar][0]
    right = tree[tar][1]

    if left != '.':
        postorder(left)

    if right != '.':
        postorder(right)

    post.append(tar)

postorder(first)
print(''.join(post))