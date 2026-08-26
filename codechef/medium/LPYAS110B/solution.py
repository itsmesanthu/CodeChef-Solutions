v= "aeiou"
w=str(input())
count=0
for i in range(len(w)):
    if w[i] in v:
        count+=1
print(count)