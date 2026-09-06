import pandas as pd

# update the code below
students = ['Student_1',"Student_2","Student_3","Student_4","Student_5"]

grades = pd.Series([85, 90, 88, 92, 95],index=students )

print(grades)