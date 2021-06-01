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

import pandas as pd

data = {'First Column Name':  ['First value', 'Second value',...],
        'Second Column Name': ['First value', 'Second value',...]}

df = pd.DataFrame (data, columns = ['First Column Name','Second Column Name',...])

print (df)

import pandas as pd

property = {'neighbourhood': ['alphabet city','Chelsea','chinatown','civic center'],
        'sale Price': [662500,3936272,8000000,11693337]
        }

df = pd.DataFrame(property, columns = ['neighbourhood', 'sale Price'])

print (df)

import pandas as pd

property = {'neighbourhood': ['alphabet city','Chelsea','chinatown','civic center'],
        'sale Price': [662500,3936272,8000000,11693337]
        }

df = pd.DataFrame( property, columns = ['neighbourhood',' sale Price'], index=['property_1','property_2','property_3','property_4'])

print (df)

import pandas as pd

property = {'neighbourhood': ['alphabet city','Chelsea','chinatown','civic center'],
        'Price': [662500,3936272,8000000,11693337],
        'sale date': [2016, 2017,2016,2017]
        }

df = pd.DataFrame(property, columns=['neighbourhood', 'sale Price', 'sale date'])

print(df)
























