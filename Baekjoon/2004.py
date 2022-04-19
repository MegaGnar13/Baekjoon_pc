n, k = map(int, input().split())

def two_cnt(num):
    cnt = 0
    while num != 0:
        cnt += num // 2
        num //= 2
    return cnt

def five_cnt(num):
    cnt = 0
    while num != 0:
        cnt += num // 5
        num //= 5
    return cnt

print(min(two_cnt(n)-two_cnt(n-k)-two_cnt(k),five_cnt(n)-five_cnt(n-k)-five_cnt(k)))