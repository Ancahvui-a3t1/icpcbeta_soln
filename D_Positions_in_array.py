n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]<=10:
          print("A[",i,"] = ",a[i],sep="")   
    