import pandas as pd
import numpy as np
import random

df = pd.read_csv('userlist.csv', index_col=False)

uni_list = ["du", "du", "kuet", "ruet", "su", "nsu", "ewu", "aiub"]

city_list = ["noakhali", "vola", "chittagang", "sylhet", "rajshaie", "barishal", "dhaka"]

sex_list = ["male", "female"]

#df.loc[df['movieId'] > 100, 'movieId'] = random.choice(listsample)

for index_label, row_series in df.iterrows():
        df.at[index_label, 'university'] = random.choice(uni_list)
for index_label, row_series in df.iterrows():
        df.at[index_label, 'city'] = random.choice(city_list)
for index_label, row_series in df.iterrows():
        df.at[index_label, 'sex'] = random.choice(sex_list)
print(df)
df.to_csv(r'userlist_updated.csv', index=False)

