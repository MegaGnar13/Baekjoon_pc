A = int(input())

dic_list = []
for i in range(A):
    B=input()
    dic_list.append(B)
new_list = list(set(dic_list))
new_list.sort(key=lambda x:(len(x),x))

for i in new_list:
    print(i)
