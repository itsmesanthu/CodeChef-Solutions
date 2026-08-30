a,b,c=map(int, input().split())
if a<b<c:
    print("Increasing")
elif a>b>c:
    print("Decreasing")
else:
    print("Neither")