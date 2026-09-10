a=int(input())
n=list(map(int,input().split()))
x=min(n)
count=n.count(x)
if count%2==0:
   print("Unlucky")
else:
   print("Lucky")
    