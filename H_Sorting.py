x=int(input())
a=list(map(int,input().split()))
i=0
for i in range(0,len(a)):
  n=a[0]
  for i in range(1,len(a)):
    if a[i]<n:
       n=a[i]
  print(n,end=" ")
  a.remove(n)