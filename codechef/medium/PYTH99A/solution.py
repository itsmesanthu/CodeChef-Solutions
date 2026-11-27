# Count how many 'o's are present in the string using a 'for' loop and 'if' condition

string = 'bolloon'

# use this variable to count occurrences of o
count_o = 0      
for i in string:
    if i=="o":
        count_o+=1
print(count_o)