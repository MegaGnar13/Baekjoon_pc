num = int(input())
people = list(map(int,input().split()))
people.sort()
minn = 0
for i in range(len(people)):
    tar = len(people)-i
    minn+= tar*people[i]
print(minn)