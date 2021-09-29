A=int(input())
stack_list=[]
for B in range(A):
    i=list(input().split())
    if i[0]=='push':
        stack_list.append(i[1])
    elif i[0] == 'top':
        if len(stack_list)==0:
            print(-1)
        else:
            print(stack_list[-1])
    elif i[0] == 'size':
        print(len(stack_list))
    elif i[0] == 'empty':
        if len(stack_list)==0:
            print(1)
        else:
            print(0)
    elif i[0] == 'pop':
        if len(stack_list)==0:
            print(-1)
        else:
            print(stack_list[-1])
            stack_list.pop()