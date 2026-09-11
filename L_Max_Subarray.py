a=int(input())
for c in range(a):
    b=int(input())
    n=list(map(int,input().split()))
    for d in n:
        print(d,end=" ")
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
           print(n[i],end=" ")
        else:
           print(n[i+1],end=" ")
    for i in range(len(n)-2):
        if n[i]<n[i+1]:
          if n[i]<n[i+2]:
            print(n[i],end=' ')
          else:
             print(n[i+2],end=" ")
        else:
           if n[i+1]<n[i+2]:
             print(n[i+1],end=" ")
           else:
             print(n[i+2],end=" ")