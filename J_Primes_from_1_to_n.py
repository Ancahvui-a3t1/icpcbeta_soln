n=int(input())
count=0
for i in range(2,n+1):
  for j in range(1,i+1):
    if i%j==0:
        count+=1
    else:
        continue
  if count==2:
        print(i,end=" ")
  else:
      continue
