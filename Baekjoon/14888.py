import itertools
A=int(input())
B=list(map(int,input().split()))
C=list(map(int,input().split()))


new_list=['+','-','*','/']

newc_list=[]
for i in range(len(C)):
    newc_list.extend(new_list[i]*C[i])

result=itertools.permutations(newc_list,A-1)
convolution=[]
for i in result:
    convolution.append(i)
convolution=list(set(convolution))
num_list=[]
for i in convolution:
    num=B[0]
    for j in range(len(i)):

        if i[j] == '+':
            num=num+B[j+1]
        elif i[j] == '*':
            num=num*B[j+1]
        elif i[j] == '/':
            if num<0:
                num=-(-num//B[j+1])
            else:
                num=num//B[j+1]
        elif i[j] == '-':
            num = num - B[j + 1]
    num_list.append(num)

print(max(num_list))
print(min(num_list))