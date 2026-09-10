x=int(input())
a=list(map(int,input().split()))
n=a[0]
m=0
for i in range(1,len(a)):
    if a[i]<n:
       n=a[i]
       m=i
print(n,m+1,sep=" ")
