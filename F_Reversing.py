n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    print(a[n-i-1],end=" ")