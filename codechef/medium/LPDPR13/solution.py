import pandas as pd

gradebook_data = [
    ['Alice', 'Math', 95],
    ['Bob', 'Math', 87],
    ['Charlie', 'Math', 91],
    ['Alice', 'Science', 92],
    ['Bob', 'Science', 88],
    ['Charlie', 'Science', 94]
]

# Update your code below
gradebook_df = pd.DataFrame(gradebook_data, columns=['Student', 'Subject', 'Grade'],index=['ID1','ID2','ID3','ID4','ID5','ID6'])
print(gradebook_df)
