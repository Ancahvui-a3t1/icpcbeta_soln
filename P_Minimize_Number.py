n=int(input())
m=input()
a=list(map(int,m.split()))
count=0
while n>0:
  for i in m:
    if int(i)%2==0:
        o=int(i)//2
        m.replace(str(o),str(i))
        count+=1
    else:
       break
print(count)