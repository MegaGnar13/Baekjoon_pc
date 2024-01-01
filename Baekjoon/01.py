a, b = map(int, input().split())
t = int(input())

tmp = b + t

if b + t >= 60:
    new_h = (b + t) // 60
    remain = (b + t) % 60

else:
    remain = b + t
    new_h = 0

next_h = a + new_h
next_m = remain

if next_h >= 24:
    last_h = next_h % 24
else:
    last_h = next_h

print(last_h, next_m)
# print(next_m)