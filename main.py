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

import pandas as pd

property = {'neighbourhood': ['alphabet city','Chelsea','chinatown','civic center'],
        'Price': [662500,3936272,8000000,11693337],
        'sale date': [2016, 2017,2016,2017]}

df = pd.DataFrame(property, columns=['neighbourhood', 'sale Price', 'sale date'])

# sort property by - ascending order
df.sort_values(by=['neighbourhood'], inplace=True)

print(df)

import pandas as pd

property = {'neighbourhood': ['alphabet city','Chelsea','chinatown','civic center'],
        'Price': [662500,3936272,8000000,11693337],
        'sale date': [2016, 2017,2016,2017]}

df = pd.DataFrame(property, columns=['neighbourhood', 'sale Price', 'sale date'])

# sort property by - descending order

df.sort_values(by=['neighbourhood'], inplace=True, ascending=False)

print (df)



import pandas as pd

property = {'neighbourhood': ['alphabet city','Chelsea','chinatown','civic center'],
        'Price': [662500,3936272,8000000,11693337],
        'sale date': [2016, 2017,2016,2017]}

df = pd.DataFrame(property, columns=['neighbourhood', 'sale Price', 'sale date'])

# sort property by - descending order

df.sort_values(by=['sale date'], inplace=True, ascending=False)

print (df)

import pandas as pd

property = {'neighbourhood': ['alphabet city','Chelsea','chinatown','civic center'],
        'sale Price': [662500,3936272,8000000,11693337]}

df = pd.DataFrame(property, columns= ['neighbourhood', 'sale Price'])

print(df)


import pandas as pd
#indexing
property = {'neighbourhood': ['alphabet city','Chelsea','chinatown','civic center'],
        'sale Price': [662500,3936272,8000000,11693337]}

df = pd.DataFrame(property, columns= ['neighbourhood', 'sale Price'])
df = df.drop([0, 2])
df = df.reset_index(drop=True)

print(df)

import pandas as pd
#grouping commission by estate agent
data = {'Month': ['Jan ','Feb ','Mar ','Apr ','May ','Jun '],
        'Estate agent 1 Commission': [1500,2200,3500,1800,3000,2800],
        'Estate agent 2 Commission': [3200,4100,2500,3000,4700,3400],
        'Estate agent 3 Commission': [1700,3100,3300,2700,2400,3100]
        }

df = pd.DataFrame(data,columns=['Month','Estate agent 1 Commission','Estate agent 2 Commission','Estate agent 3 Commission'])
print (df)

import pandas as pd
#remove duplicates
property = {'type': ['2 bed','3 bed','4 bed','4 bed','2 bed','1 bed','2 bed','4 bed'],
         'neighbourhood': ['Chelsea','Chinatown','Chinatown','Chelsea','Alphabet city','civic center','Chinatown','Chelsea']
        }
df = pd.DataFrame(property, columns = ['type', 'neighbourhood'])

df_duplicates_removed = df.drop_duplicates()
print(df_duplicates_removed)






















