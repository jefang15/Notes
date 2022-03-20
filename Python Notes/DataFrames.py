""" Python Notes - DataFrames """



" Create DataFrame "

# From scratch
import pandas as pd
import numpy as np

df=pd.DataFrame({
    'x_values': range(1,101), 
    'y_values': np.random.randn(100)*15+range(1,101), 
    'z_values': (np.random.randn(100)*15+range(1,101))*2 })
print(df)

# Set data types
df = pd.DataFrame(
    {
        'column1': pd.Series([], dtype='str'),
        'column2': pd.Series([], dtype='object'),
        'column3': pd.Series([], dtype='int'),
        }
    )

# Dataframe from List / List to Dataframe
column_names = ['column1', 'column2', 'column3']
new_data = pd.DataFrame(list, columns=column_names)

# Append one DataFrame to existing DataFrame
df_merge = pd.concat([df, new_df], ignore_index=True)



" Show "

# Datatypes of each column 
df.dtypes

# Show object type
type(df)

# Show all Columns
df.columns
list(df.columns.values)

# Show first n observations
df.head(30)


" Print as Table "

from tabulate import tabulate

print(tabulate(df, headers='keys', tablefmt='plain'))
"""
tablefmt options:
“plain”
“simple”
“github”
“grid”
“fancy_grid”
“pipe”
“orgtbl”
“jira”
“presto”
“pretty”
“psql”
“rst”
“mediawiki”
“moinmoin”
“youtrack”
“html”
“latex”
“latex_raw”
“latex_booktabs”
“textile”
"""



" Sort "

# Ascending
df = df.sort_values(by='Column')

# Descending
df = df.sort_values(by='Column', ascending=False)

# Multiple columns
df = df.sort_values(by=['Video', 'Date']).reset_index(drop=True)



" Merge "

# Two DataFrames
df = (
    left=dr_primary
    right=df_secondary,
    how='left',  # left, right, inner join, etc
    left_on='Date',  # Common key
    right_on='Date'  # Common key
    )

# More than two DataFrames
df_final = df1[['a', 'b', 'c']].merge(
    df2[['d', 'e', 'f']], how='left', on=['a']).merge(
    df3, how='left', on=['a']
    )
    # e.g.
    df_key = df[['Buyer', 'Seller', 'Volume']].merge(
        label_key_df[['Name', 'Buyer Key']], how='left', left_on=['Buyer'], right_on=['Name'])

# Without common key
from intertools import product
prod = product(df['a'], df2['b'])
pd.DataFrame(list(prod), columns=['a', 'b'])



" Rearrange Columns "
df = df[['a', 'b', 'c']]



" Rename Columns "
df.rename(
    columns =
    {'Old1' : 'New1',
     'Old2' : 'New2'}
    , inplace=True)



" Delete Data "

# Delete columns / delete fields / drop columns / drop fields
del df['Column']
df_new = df.drop(columns='column1')

# Delete row based on value
df = df[df.Date != '2022-01-30 00:00:00']

# Delete multiple columns
df = df.drop(columns=['column1', 'column2', 'column3'])
df.drop(columns=['column1', 'column2', 'column3'], inplace=True)  # Instead of creating new df, modifies current

# Delete multiple columns via list
columns_to_drop = ['column1', 'column2', 'column3']
df = df.drop(columns=columns_to_drop)

# Delete NA / delete NULL
df = df[df['Column'].notna()]
df.dropna(inplace=True)

# Delete rows / drop rows by index number
df = df.drop(159)

# Difference between one row and previous row, within groups
df['Views_Delta'] = df.groupby('Video')['Views'].diff()

# Remove duplicates
df = df.drop_duplicates('Column', keep='first')  # One column
df = df.drop_duplicates(['ColumnA', 'ColumnB'], axis=1, keep='first')  # One column



" Convert "
# Float to integer
df['float'] = df['int'].astype(int)

# String to integer
df['Views'] = pd.to_numeric(df['Views'])



" Filter "

# By numeric / by number
df = df.loc[(df['column1'] == 13948)]

# By string
df = df.loc[(df['column1'] == 'RT')]
df = df.loc[(df['column1'] == 'A') | (df['Name'] == 'B')]

# Contains
df = df.loc[(df['String'].str.contains('Name', na=False))]
df = df.loc[(df['String'].str.contains('A | B | C', na=False))]

# By datetime
df= df.loc[(df['Date'] >= '2016-01-01 00:00:00')]

# By date range
out = df.query('Date >= "2016-01-01 00:00:00" and Date < "2017-01-01 00:00:00')

# By multiple criteria (and)
df = df.loc[(df['a'] == 15) & (df['b'] == 'A')]

# By multiple criteria (or)
df = df.loc[(df['a'] == 15) | (df['b'] == 'A')]

# By items in a list
list = ['a', 'b', 'c']  # Create list
df = df[df['Column'].isin(list)]

# By items not in a list
df = df[~df['Column'].isin(list)]

# Null
df = df[(df['Column'].isnull())]

# Subset
df_wide = df[["keep_column1", "keep_column2", "keep_column3"]]

# Unique entries in column
df_export["Video"].unique()  # To array
pd.DataFrame(df_export["Video"].unique())  # To dataframe



" Format "
# Integer with commas
df["Views_Delta"] = df.Views_Delta.apply(lambda x : "{:,}".format(x))



" Group By "

# Average
df.groupby(['a', 'b']).mean().reset_index()

# Count
df.groupby(['a', 'b']).count().reset_index()

# Sum
df.groupby(['a', 'b']).sum().reset_index()
df = df.groupby(['Month_Year', 'Video'])["Views_Delta"].sum().reset_index()  # Group by Month_Year and Video columns, then sum Views_Delta column

# Count of unique
df["A"].nunique()



" If then / If/Then "

# Create new string column based on condition
df.loc[df['ColumnA'] >= df['condition'], 'new_column'] = 'Text'

# Create new numeric column based on difference / sum / product of other columns
df.loc[
    df['ColumnA'] >= df['ColumnB'],
    'new_column'] = (df['ColumnA'] - df['ColumnB'])

# Create new numeric column based on multiple conditions
df.loc[
    (df['ColumnA'] >= df['ColumnB']) &
    (df['ColumnB'] >= 14) &
    (df['ColumnC'] >= '2016-01-01 00:00:00'),
    'new_column'] = (df['ColumnA'] - df['ColumnB'])



" Melt / Transpose"

# Long to wide
df_wide = df.pivot(
    index="Date",
    columns="Video",
    values="Views"
    ).reset_index()

# Wide to long
df_long = df.melt(
    id_vars=['a', 'b'],  # These variable are not pivoted; can use a list of variables here
    value='c',  # These variables are pivoted
    value_name='Hour_'  # Rename
    )



" Datetime and Dates "

# Extract Year
df["Year"] = df["Date"].dt.year

# Extract Month
df["Month"] = df["Date"].dt.month

# Extract Day
df["Month"] = df["Date"].dt.date
df["Month"] = df["Date"].dt.day

# Format Date
DateFormatter('%b %d, %Y')  # Month (three-letter month) day, and year
DateFormatter('%Y-%m-%d')  # Year-Month-Day (all numbers)

# Range of dates
df = pd.DataFrame({'Dates' : pd.date_range('2021-01-01', periods=28)})  # Creates 28 days by day from Jan 1, 2021



" Other "

# Reset index
df = df.reset_index(drop=True)

# Round number
df = df['ColumnA'].round(2)

# Absolute value
df['Amount'] = df['Amount'].abs()

# Remove characters from string / keep only numeric
df['Column'] = df['Column'].extract('(\d+)')

# Length
len(df)
