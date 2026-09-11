a=list(map(int,input().split()))
n=input()
count=0
if n[a[0]]!="-":
    print("No")
else:
  for i in n:
       while i!="-":
         if int(i)<=9 or int(i)>=0:
          if len(n)==a[0]+a[1]+1:
              count+=1
         else:
              print("No")
if count==len(n)-1:
  print("Yes")