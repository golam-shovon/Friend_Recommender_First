import pandas as pd
import numpy as np
import random

df = pd.read_csv('friendlist.csv', index_col=False)

listsample = list(range(1, 50))


#df.loc[df['movieId'] > 100, 'movieId'] = random.choice(listsample)

for index_label, row_series in df.iterrows():
        df.at[index_label, 'id'] = random.choice(listsample)
for index_label, row_series in df.iterrows():
        df.at[index_label, 'fid'] = random.choice(listsample)

print(df)
df.to_csv(r'friendlist_updated.csv', index=False)