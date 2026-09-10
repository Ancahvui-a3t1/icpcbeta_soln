a=int(input())
for c in range(a):
 b=int(input())
 n=list(map(int,input().split()))
 v=0
 for i in range(len(n)):
    for j in range(i+1,len(n)):
        v=n[i]+n[j]+j-i
        if z>v:
          z=v
print(z)