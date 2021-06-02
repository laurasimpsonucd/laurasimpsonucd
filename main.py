# See PyCharm help at https://www.jetbrains.com/help/pyc
import pandas as pd

df = pd.read_csv("nyc_rolling_sales")
print(df)

data = pd.read_csv("nyc_rolling_sales")
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

import pandas as pd
#replace values
property = {'first_set':  ['Chelsea','Chinatown','Alphabet city','civic center'],
          'second_set': ['Cork', 'Dublin', 'waterford', 'Kerry']
         }

df = pd.DataFrame(property, columns= ['first_set','second_set'])
df['first_set'] = df['first_set'].replace(['Chelsea','Cork'],['Chinatown','Kerry'])

print (df)

import pandas as pd
#loop and iterrows
#create dataframe
df_marks = pd.DataFrame({
'borough': ['Chinatown', 'Chelsea', 'Alphabet city', 'Civic center'],
'sales': [5, 74, 17, 38]})


for index, row in df_marks.iterrows():
    print(index, ': ', row['borough'], 'has', row['sales'], 'sales.')


#merge dataframes
import pandas as pd

clients = {'buyer_ID': [1221,1222,1333,2444,7555],
           'buyer_Name': ['John smith','Mary Black', 'Bill Rodger','Rachel Adams','Pamela Anderson']
           }
df1 = pd.DataFrame(clients, columns= ['buyer_ID','buyer_Name'])
print(df1)

countries = {'Buyer_ID': [111,222,333,444,777],
             'Buyer_Country': ['UK','Italy','Spain','Ireland','France']
             }
df2 = pd.DataFrame(countries, columns= ['Client_ID', 'Client_Country'])
print(df2)




#dictionary

import pandas as pd

my_dict = {'rental':1500,'commercial':2000,'land':5000,'office space':3000}
df = pd.DataFrame(list(my_dict.items()),columns = ['category','sale Price'])

print (df)
print (type(df))

#list
from pandas import DataFrame

People_List = [['Jon','Mark','Maria','Jill','Jack'],['Smith','Brown','Lee','Jones','Ford'],[21,38,42,28,55]]

df = DataFrame (People_List).transpose()
df.columns = ['First_Name','Last_Name','Age']
print (df)

#numpy
import numpy as np
import pandas as pd
my_array = np.array([[11,22,33],[44,55,66]])

df = pd.DataFrame(my_array, columns = ['Column_A','Column_B','Column_C'], index = ['Item_1', 'Item_2'])

print(df)
print(type(df))

import numpy as np
import pandas as pd
my_array = np.array([[11,22,33],[44,55,66]])

df = pd.DataFrame(my_array, columns = ['Column_A','Column_B','Column_C'], index = ['Item_1', 'Item_2'])

print(df)
print(type(df))

import matplotlib.pyplot as plt
#bar chart
area = ['chinatown', 'Civic center', 'albhapet city', 'chelsea']
USD_average = [45000, 42000, 52000, 49000]

xAxis = [i + 0.5 for i, _ in enumerate(area)]

plt.bar(xAxis, USD_average, color='teal')
plt.title('area Vs USD average', fontsize=14)
plt.xlabel('area', fontsize=14)
plt.ylabel('USD average', fontsize=14)
plt.xticks([i + 0.5 for i, _ in enumerate(area)], area)
plt.show()

import matplotlib.pyplot as plt
#scatter plot
commission_Rate = [11.1, 12.8, 5.7, 15.7, 10.8,]
house_Index_Price = [15000000, 152000000, 152500000, 152300000, 15150000]

plt.scatter(commission_Rate, house_Index_Price, color='red')
plt.title('commission Rate Vs house Index Price', fontsize=14)
plt.xlabel('commission Rate', fontsize=14)
plt.ylabel('house Index Price', fontsize=14)
plt.grid(True)
plt.show()




















