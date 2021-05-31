# See PyCharm help at https://www.jetbrains.com/help/pyc
import pandas as pd

df = pd.read_csv("nyc-rolling-sales.csv")
print(df)

data = pd.read_csv("nyc-rolling-sales.csv")
print(data)

import pandas as pd
df = pd.DataFrame(data, columns= ['BOROUGH','SALE Price', 'SALE DATE'])
print (df)

import pandas as pd
df = pd.DataFrame(data, columns= ['NEIGHBOURHOOD','SALE Price', 'SALE DATE'])
print (df)

import pandas as pd
df = pd.DataFrame(data, columns= ['category','SALE Price', 'SALE DATE'])
print (df)

import pandas as pd
df = pd.DataFrame(columns= ['category', 'sale Price','sale date'])
df.sort_values(by=['category'], inplace=True)
print (df)















