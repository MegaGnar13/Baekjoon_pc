import sys
num = int(sys.stdin.readline())
ss = set()
for _ in range(num):
    a = list(sys.stdin.readline().split())

    if a[0] == 'add':
        if a[1] in ss:
            continue
        else:
            ss.add(a[1])

    if a[0] == 'remove':
        ss.discard(a[1])
    if a[0] == 'check':
        if a[1] in ss:
            print(1)
        else:
            print(0)
    if a[0] == 'toggle':
        if a[1] in ss:
            ss.remove(a[1])
        else:
            ss.add(a[1])
    if a[0] == 'all':
        ss = {str(i) for i in range(1,21)}

    if a[0] == 'empty':
        ss.clear()
