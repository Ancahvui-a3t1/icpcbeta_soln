a=int(input())
for c in range(a):
  b=int(input())
  n=list(map(int,input().split()))
  z=n[0]+n[1]+1
  for i in range(b):
    for j in range(i+1,b):
        v=n[i]+n[j]+j-i
        if z>v:
          z=v
  print(z)