import pandas as pd

data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')

result = data_frame.groupby('Name').sum()

num_group = len(result)

print(num_group)