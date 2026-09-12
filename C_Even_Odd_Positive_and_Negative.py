n=int(input())
a=list(map(int,input().split()))
even,odd,pos,neg=0,0,0,0
for i in a:
    if i==0:
        even+=1
    elif i>0:
        pos+=1
        if i%2==0:
            even+=1
        else:
            odd+=1
    elif i<0:
        neg+=1
        if i%2==0:
            even+=1
        else:
            odd+=1
print("Even:",even)
print("Odd:",odd)
print("Positive:",pos)
print("Negative:",neg)