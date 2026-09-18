n=list(map(int,input().split()))
count,j=0,0
for i in range(n[0],n[1]+1):
     g=i
     while g>0:
          j+=1
          n=g%10
          g=g//10
          if n==4 or n==7:
            count+=1
     if count==j:
       print(i,end="\n")
       
            
