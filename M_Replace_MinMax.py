a=int(input())
m=input()
n=list(map(int,m.split()))
b=max(n)
c=min(n)
for i in range(a):
    if n[i]==b:
        n[i]=c
    elif n[i]==c:
        n[i]=b
for j in n:
    print(j,end=" ")