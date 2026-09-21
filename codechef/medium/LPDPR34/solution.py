import pandas as pd
import numpy as np

# Generating the data
n = 1_000_000
data = np.random.choice(['Apple', 'Banana', 'Cherry'], size=n)

# Without Categorical
df = pd.DataFrame({'Fruit': data})
print("Memory usage without Categorical:")
print(df.memory_usage(deep=True))

# With Categorical
df['Fruit'] = df['Fruit'].astype('category')
print("\nMemory usage with Categorical:")
print(df.memory_usage(deep=True))
