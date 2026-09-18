n=list(map(int,input().split()))
a=[]
for i in n:
    for j in range(1,i//2+1):
        if i%j==0:
            a.append(j)
            

