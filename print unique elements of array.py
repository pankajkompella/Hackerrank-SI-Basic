n=int(input())
c=[]
a=list(map(int,input().split()))
for i in range(n):
    b=a.count(a[i])
    if(b==1):
        c.append(a[i])
for k in c:
    print(k,end=" ")
