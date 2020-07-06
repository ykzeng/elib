import pandas as pd
import sys

src = sys.argv[1]
cols = sys.argv[2]
dest = sys.argv[3]

cols = cols.split(',')
df=pd.read_csv(src, encoding='iso-8859-1')
for c in cols:
    df[c] = df[c].str.encode('utf-8','ignore').str.decode('iso-8859-1')
df.to_csv(dest, encoding='utf-8')