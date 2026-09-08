x=int(input())
a=list(map(int,input().split()))
for i in range(len(a)-2):
    n=a[i]
    if a[i+1]<n:
       n=a[i+1]
    else:
       if a[i+2]<n:
            n=a[i+2]
print(n,a.index(n)+1,sep=" ")