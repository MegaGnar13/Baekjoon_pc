def seq(arr,tar):
    tar1=0
    tar2=1
    now=arr[tar1]+arr[tar2]
    while now!=tar:
        if now<tar:
            tar1+=1
            tar2+=1
            now = arr[tar1] + arr[tar2]
        else:
            tar1-=1
            now = arr[tar1] + arr[tar2]


    return [tar1,tar2]

print(seq([1,4,7,15,37,42],22))