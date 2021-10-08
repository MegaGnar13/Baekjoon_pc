import itertools        #itertools의 combination 사용
N,M=map(int,input().split())        #N:city size M:chicken집 개수
city=[]
for i in range(N):
    city.append(list(map(int,input().split())))     #city를 list로 생성

home=[]
chick=[]                #city중 1은 home 2는 chick집
for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            home.append([i,j])
        if city[i][j]==2:
            chick.append([i,j])

stay_ch=itertools.combinations(chick,M)     #chick집 조합

answer=[]
for i in stay_ch:       #chick 조합중 1개
    chmin = []
    for j in home:      #각 집마다 chick과의 거리 구함
        ch_list = []
        for k in i:
            ch_list.append(abs(k[0]-j[0])+abs(k[1]-j[1]))
        chmin.append(min(ch_list))      #한 집에서 모든 뽑힌chick 조합중 가장 가까운 거리
    answer.append(sum(chmin))       #모든 집에서 최소거리 합
print(min(answer))          #모든 chick 조합 중 가장 최소