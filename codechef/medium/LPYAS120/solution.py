n = int(input())
i=1
n1,n2=0,1
while i<=n:
    temp=n1+n2
    print(n1,end=" ")
    n1=n2
    n2=temp
    i+=1
    