def asal_mi(x):
    for i in range(x):
        if i>1 and x%i!=0 and x!=2:
            k=1
        if x==2:
            k=1
        if i>1 and x%i==0 and x!=2:
            k=0
            return 0
    return k
sayi=0
while(sayi!=-1):
    a=input()
    sayi=int(a)
    ctr=asal_mi(sayi)
    if ctr==1:
        print("asal")
    elif ctr==0:
        print("asal değil")
