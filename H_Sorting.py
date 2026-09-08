x=int(input())
a=list(map(int,input().split()))
i=0
n=0
while i>=0:
  for i in range(len(a)-2):
    n=a[i]
    if a[i+1]<n:
       n=a[i+1]
    else:
       if a[i+2]<n:
          n=a[i+2]
  print(n,end=" ")
  a.remove(n)