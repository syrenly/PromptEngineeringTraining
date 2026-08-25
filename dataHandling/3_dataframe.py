# dataframe = 2-dimensional table having rows to show records and column that shows attributes
# numpy arrays are like plain tables or grid, while dataframe are smart tables with labels

import pandas as pd

# create a dictionary
data={
    "name": ["Aline", "Sarah", "John"], 
    "marks":[85,98,78],
    "subjects":["English","Math","Science"]
}

# create dataframe
df=pd.DataFrame(data)
print(df)
# output:
#     name  marks subjects
# 0  Aline     85  English
# 1  Sarah     98     Math
# 2   John     78  Science
# see that there is index, automatically created; it is not part of the data, but of the dataframe

print(df.columns) # Index(['name', 'marks', 'subjects'], dtype='str')
print("\nUsing .loc:")
# use index to retrieve data. 
# `loc` property accesses a group of rows and columns by label(s) or a boolean array.
print(df.loc[0])
# name          Aline
# marks            85
# subjects    English
# Name: 0, dtype: object

print(df.loc[[True,False,True]]) # jump middle row
#     name  marks subjects
# 0  Aline     85  English
# 2   John     78  Science

print(df.loc[1:2]) # use range
#     name  marks subjects
# 1  Sarah     98     Math
# 2   John     78  Science

print(df.loc[1:2,["name","marks"]]) # use range plus choose columns
#     name  marks
# 1  Sarah     98
# 2   John     78

# `iloc` property is a purely integer-location based indexing for selection by position.
print(df.iloc[0]) # same as loc[0]
# name          Aline
# marks            85
# subjects    English
# Name: 0, dtype: object

print(df.iloc[0:2,0:2]) # first 2 rows, first 2 attributes
#     name  marks
# 0  Aline     85
# 1  Sarah     98