import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./datasets/stocks.csv")

# print(df.head(3)) # view top of data
# print(df.tail(3)) # view bottom of data

# print(df.columns) # heading the headers

# print(df['Year']) # find specific column
# print(df.Year) # same as above but wtf, NEVER USE
# print(df['Year'][0:5]) # read specific range

# print(df.iloc[1]) # print each row or multiple rows
# print(df.iloc[0:4]) # print range of rows
# print(df.iloc[2, 0]) # specific location (Row, Column)
# print(df.loc[df['Year']==2000]) # finding specific data

# df['Total'] = df['Apple']+df['Barclays']+df['British Gas']
# print(df)

# print(df.describe()) # prints stats for the data

# # iterating through each row
# for index, row in df.iterrows():
#     print(index, row['Apple'])





# removing and setting index
def index_remove():
    print("This is the data with the index removed")
    df1 = pd.read_csv("./datasets/stocks.csv", index_col=0)
    print(df1)
    df2 = pd.read_csv("./datasets/stocks.csv").set_index("Year")
    print(df2)

index_remove()