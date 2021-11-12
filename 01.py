def circular(n):
    n=list(str(n))
    result=[]
    cnt=0
    while cnt<len(n):
        a=''.join(n)
        result.append(int(a))
        b=n[0]
        del n[0]
        n.append(b)
        cnt+=1
    return result

def prime(n):
    cnt=0
    for i in range(2,n):
        if n%i==0:
            cnt+=1
    if cnt==0:
        return True
    else:
        return False

def circular_prime(n):
    cir=circular(n)
    cnt=0
    for i in cir:
        if prime(i)==True:
            cnt+=1
    if cnt==len(cir):
        return True
    else:
        return False


print(circular(123))
print(circular(1123))
print(prime(2))
print(prime(3))
print(prime(4))
print(circular_prime(197))
print(circular_prime(13))
print(circular_prime(19))