w, h, x, y, p = map(int,input().split())

answer = 0

def rec(tar_x, tar_y):
    if x<= tar_x <= x+w and y <= tar_y <= y+h:
        return False
    else:
        return True

def cir1(tar_x, tar_y):
    tx = (tar_x - (x+w)) ** 2
    ty = (tar_y - (y + h / 2)) ** 2
    z = (tx + ty) ** 0.5

    if z <= h / 2:
        return False
    else:
        return True

def cir2(tar_x, tar_y):
    tx = (tar_x - x) ** 2
    ty = (tar_y - (y+h/2)) ** 2
    z = (tx + ty)** 0.5

    if z <= h/2:
        return False
    else:
        return True

for i in range(p):
    tar_x, tar_y = map(int,input().split())

    if not rec(tar_x,tar_y):
        answer += 1
        continue
    if not cir1(tar_x,tar_y):
        answer += 1
        continue
    if not cir2(tar_x,tar_y):
        answer += 1
        continue

print(answer)
