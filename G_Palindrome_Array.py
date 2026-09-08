n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]==a[n-i-1]:
       if n==i+1:
         print("YES")
    else:
         print("NO")
         break
    