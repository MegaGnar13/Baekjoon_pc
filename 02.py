def change_currency(sentence, rate):
    menu_1 = sentence.splitlines()
    menu_dic = []
    for i in menu_1:
        i = i.split()
        menu_dic.append([i[0],i[2]])
    print(menu_dic)

    answer=[]
    for i in menu_dic:
        i[1]=float(i[1])
        i[1]*=rate
        i[1]=str(i[1])
        aa=' '.join([i[0],':',i[1],'KWN'])
        answer.append(aa)
    rrr='\n'.join(answer)
    return rrr

menu = """Apple : 1.5 USD
Banana : 1 USD
Cake : 7 USD
"""

usd = 1200.0 # 1usd = 1200kwn
result = change_currency(menu, usd)
print(result)