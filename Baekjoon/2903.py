target = int(input())

t= 0
n = 2
m = 1

while t < target:
    n = n + m
    m = n-1
    t += 1

print(n**2)