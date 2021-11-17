def load_dict(filename):
    answer={}
    with open(filename, "rt") as f:
        a=f.read()
    b=a.splitlines()
    for i in range(len(b)):
        c=b[i].split(':')
        answer[c[0]]=c[1]
    return answer
def save_dict(filename, my_dict):
    with open(filename,'wt') as f:
        for i in my_dict:
            print(i,':',my_dict[i])
    pass

my_dict = load_dict('mydictionary.txt')
my_dict['strawberry'] = "A strawberry is a small red fruit which is soft and juicy and has tiny yellow seeds on its skin."
save_dict('mydictionary.txt', my_dict)
# http://10.150.4.67/files/본인학번_dict.txt 을 접속하여 잘 저장되었는지 확인 (예:  http://10.150.4.67/files/202111000_dict.txt )

my_dict = load_dict('mydictionary.txt')
my_dict['test'] = "test."
save_dict('mydictionary.txt', my_dict)
# http://10.150.4.67/files/본인학번_dict.txt 을 접속하여 잘 저장되었는지 확인