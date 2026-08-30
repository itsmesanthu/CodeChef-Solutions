values = list(map(int, input().split()))
for i in values:
    if i>10:
        continue
    print(i**2)