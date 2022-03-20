""" Python Notes """

""" PyCharm IDE Commands """
# Actions: Shift + Command + A
# Add line below: Command + Enter
# Comment out text: Put caret at end of line then press Command + /
# Download Modules: View > Tool Windows > Python Packages
# Download Packages: Command + Comma > Project > Python Interpreter
# Run single line of code ("Execute Selection in Python Console"): Shift + Enter
# Keymap: Comment + , > Keymap
# Plugins: Command + , > Plugins
# Preferences: Command + ,
# Vertical Selection: Command + Shift + 8
# GitHub (https://pythonfusion.com/pycharm-project-on-github/)
#   New Project: VCS > Create Git Repository > Set project path > GitHub > Share Project on GitHub
#   Existing Projects already on GitHub: Commit (to show files that have changed) > Check files that have changed >
#   Click Commit and Push > Push
# Multiple statements on one line
    # y = 3; x = 4; print(x+y)
# Toggle Zen Mode: Fn + F8


""" PyCharm Customize Settings """
# Functions
    # 88C0D0 (blue)
# Text within triple and double quotes: Preferences > Editor > Color Scheme > Python > String > Text (unicode)
    # A3BE8C (green)
    # D7BA7D (mustard)
# Numbers: Preferences > Editor > Color Scheme > Python > Number
    # B48EAD (purple)
    # EF9E4F (orange)
    # F1969F (pink)
# Highlight: Preferences > Editor > General > Selection Background
    # BF616A (pepto bismol)
    # 10A5BD (bright blue)


""" Check Python Version """
import sys

print(sys.version)
# 3.9.3 (v3.9.3:e723086bc3, Apr  2 2021, 08:25:55)
print(sys.executable)





""" Packages """
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession  # run "pip install requests-html" in terminal if needed.





""" Strings """

# Hello World
print('Hello, world')

# Print
msg = "Hello World"
print(msg)

# New line in string
print("New /n line")

# Print literal characters
print('New /"line')

# Format numeric with commas
print(100000)
print(f'{100000:,}')

# Split string by word instead of characters
pdf_text_words = pdf_text.split()




""" Class """

# Creates a new data type (beside string, numeric, boolean)
class Student:  # Student - name of class
    def __init__(self, name, major, gpa):  # initialize function and define "student"
        self.name = name  # each student has a name
        self.major = major  # each student has a major
        self.gpa = gpa  # each student has a gpa

# Objects within the class
student1 = Student('Jim', 'Business', 4.0)  # student1 is an object - an actual student
print(student1.name)  # can call specific qualities of this student





""" DataFrame """

# Append to existing DataFrame
df_merge = pd.concat([existing_df, new_data], ignore_index=True)

# Create and set data type from scratch
df = pd.DataFrame(
    {
        'Channel': pd.Series([], dtype='str'),
        'Video': pd.Series([], dtype='str'),
        'Upload Date': pd.Series([], dtype='object'),
        'Duration': pd.Series([], dtype='str'),
        'Views': pd.Series([], dtype='int'),
        'Likes': pd.Series([], dtype='int'),
        'Dislikes': pd.Series([], dtype='int'),
        }
    )

df = pd.DataFrame({
    'x_values': range(1, 101),
    'y_values': np.random.randn(100) * 15 + range(1, 101),
    'z_values': (np.random.randn(100) * 15 + range(1, 101)) * 2})

# Create DataFrame from List / List to Dataframe
df_columns = ['Date', 'Channel', 'Title', 'Duration', 'Views', 'Likes', 'Dislikes', 'Upload Date']
new_data = pd.DataFrame(list_of_video_names, columns=df_columns)

# Columns
df.columns
list(df.columns.values)

# Convert float to integer
df["Views_Delta"] = df["Views_Delta"].astype(int)

# Convert string to numeric
df['Views'] = pd.to_numeric(df['Views'])

# Datatype
df.dtypes

# Delete columns / delete fields / drop columns / drop fields
# Delete single column
del df['Column']
df_new = df.drop(columns='a')

# Delete row based on value
existing_df = existing_df[existing_df.Date != '2022-01-30 00:00:00']

# Delete multiple columns
df = df.drop(columns=['a', 'b', 'c'])
df = df.drop(columns=['a', 'b', 'c'], inplace=True)  # Instead of creating new df, modifies current

# Delete multiple columns via list
columns_to_drop = ['a', 'b', 'c']  # Create list of variable names to drop
df = df.drop(columns=columns_to_drop)  # call the list in the drop function

# Delete na / delete null
df = df[df['Column'].notna()]

# Delete rows / drop rows
df = df.drop(159)  # Drop by index number

# Difference between rows within groups
df['Views_Delta'] = df.groupby('Video')['Views'].diff()

# Drop na / delete rows with na
df.dropna(inplace=True)

# Filter

    # By numeric / by number
    df = df.loc[(df['ID'] == 13948)]

    # By string
    df = df.loc[(df['Name'] == 'RT')]
    df = df.loc[(df['Name'] == 'A') | (df['Name'] == 'B')]

    # By datetime
    df= df.loc[(df['Date'] >= '2016-01-01 00:00:00')]

    # By date range
    out = df.query('Date >= "2016-01-01 00:00:00" and Date < "2017-01-01 00:00:00')

    # By multiple criteria (and)
    df = df.loc[(df['a'] == 15) & (df['b'] == 'A')]

    # By multiple criteria (or)
    df = df.loc[(df['a'] == 15) | (df['b'] == 'A')]

    # By list
    list = ['a', 'b', 'c']  # Create list
    df = df[df['Column'].isin(list)]

    # Not in list
    df = df[~df['Column'].isin(list)]

    # Contains
    df = df.loc[(df['String'].str.contains('Name', na=False))]
    df = df.loc[(df['String'].str.contains('A | B | C', na=False))]

    # Null
    df = df[(df['Column'].isnull())]

# Format integer with commas
df["Views_Delta"] = df.Views_Delta.apply(lambda x : "{:,}".format(x))

# Group by

    # Average
    df.groupby(['a', 'b']).mean().reset_index()

    # Count
    df.groupby(['a', 'b']).count().reset_index()

    # Sum
    df.groupby(['a', 'b']).sum().reset_index()
    df = df.groupby(['Month_Year', 'Video'])["Views_Delta"].sum().reset_index()  # Group by Month_Year and Video columns,
    # sum Views_Delta column

    df["A"].nunique()  # Count of unique

# If then / If/then

    # Create new text column based on condition
    df.loc[
        df['ColumnA'] >= df['ColumnB'],
        'ColumnC'] = 'Text'

    # Create new numeric column based on difference / sum / product of other columns
    df.loc[
        df['ColumnA'] >= df['ColumnB'],
        'ColumnC'] = (df['ColumnA'] - df['ColumnB'])

    # Create new numeric column based on multiple conditions
    df.loc[
        (df['ColumnA'] >= df['ColumnB']) &
        (df['ColumnB'] >= 14) &
        (df['ColumnC'] >= '2016-01-01 00:00:00'),
        'ColumnC'] = (df['ColumnA'] - df['ColumnB'])

# Melt / transpose long to wide
df_wide = df.pivot(
    index="Date",
    columns="Video",
    values="Views"
    ).reset_index()

# Melt / transpose wide to long
df_long = df.melt(
    id_vars=['a', 'b'],  # These variable are not pivoted; can use a list of variables here
    value='c',  # These variables are pivoted
    value_name='Hour_'  # Rename
    )

# Merge

    # Two datasets
    df = (
        left=dr_primary
        right=df_secondary,
        how='left',  # left, right, inner join, etc
        left_on='Date',  # Common key
        right_on='Date'  # Common key
        )

    # More than two datasets
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

# Print as table
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

# Rearrange
df = df[['a', 'b', 'c']]

# Rename
df.rename(
    columns =
    {'Old1' : 'New1',
     'Old2' : 'New2'}
    , inplace=True)

# Remove characters from string / keep only numeric
df['Column'] = df['Column'].extract('(\d+)')

# Remove duplicates
df = df.drop_duplicates('Column', keep='first')  # One column
df = df.drop_duplicates(['ColumnA', 'ColumnB'], axis=1, keep='first')  # One column

# Reset index
df = df.reset_index(drop=True)

# Round number
df = df['ColumnA'].round(2)

# Show first n observations
df.head(31)

# Sort

    # Ascending
    df = df.sort_values(by='Column')

    # Descending
    df = df.sort_values(by='Column', ascending=False)

    # Multiple columns
    df = df.sort_values(by=['Video', 'Date']).reset_index(drop=True)

# Subset
df_wide = df[["Date", "Jesus, Take The Wheel", "Don't Forget To Remember Me", "Before He Cheats", "Wasted"]]

# Unique entries in column
df_export["Video"].unique()  # To array
pd.DataFrame(df_export["Video"].unique())  # To dataframe

# Absolute value
freedom_unlimited['Amount'] = freedom_unlimited['Amount'].abs()





""" Dictionary """
# Dictionary keys (keys can be numbers or strings) must be unique

# Create dictionary
month_conversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March'
    # 'Jan' - key
    # 'January' - value
    }

# Print specific value based on the key
print(month_conversions['Jan'])



""" Datetime and Dates """

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



""" Functions """

# Sample function
def bio(name, age):
    print(name + " is " + age + " years old.")
    # def - call function
    # greet - name of function
    # name - what to include when calling this function

bio('John', '35')





""" Import and Export Data (Save Data) """

# Import CSV
df = pd.read_csv("YouTube Views.csv")
# Import Excel
df = pd.read_excel("YouTube Views.xlsx")

# Export CSV
df.to_csv("YouTube Views.csv", index=False)

# Export Excel
df.to_excel("YouTube Views.xlsx", index=False)





""" Length """

# Length of rows in dataset
len(df)

# Length of string
len('Hello, world')

# Length of list
names_list = ['John', 'James', 'Joel']
len(names_list)





""" Lists / Arrays """

# Add item to list of strings
list.append('Cal')

# Add item to list of strings in a specific position
list.insert(0, 'Al')

# Assign numbers to each item
# https://stackoverflow.com/questions/42350029/assign-a-number-to-each-unique-value-in-a-list
label = {ni: indi for indi, ni in enumerate(set(source_list))}
label_key = [label[ni] for ni in source_list]

# Create list from dataframe column
key_volume = list(df_key['Volume'])

# Create list of numbers
prime_numbers = [1, 3, 5, 7, 11, 13, 17, 19]
print(prime_numbers)

# Create list of strings
names_list = ['John', 'James', 'Joel']
print(names_list)

# Indexing
list = ['Apple', 'Banana', 'Orange']

print(list[0])  # First item in list
print(list[1])  # Second item in list
print(list[-1])  # Last from list
print(list[2:5])  # Range of items. Returns third, fourth, and fifth items
print(list[:4])  # First n items. Returns first through 4th item
print(list[4:])  # Last n items. Returns 4th through last item

# Remove item from list of strings
names_list.remove('Cal')





" Operators "

# Not equal: !=




""" Loops """

" For Loop "
friend = ['Jim', 'Kristine', 'Tim']
for name in friend:  # for every name in the friend list, do
    print(name)  # print





""" Strings """

# Replace symbols in string
new_data['Title'] = new_data['Title'].str.replace(".*(- )", "")  # Remove everything before hyphen via .* before the parentheses.
new_data['Title'] = new_data['Title'].str.replace("(\().*", "")  # Remove everything after the first open parenthesis
# "/("
new_data['Title'] = new_data['Title'].str.replace("(ft.).*","")   # Remove everything after the string "ft."
new_data['Title'] = new_data['Title'].str.rstrip(" ")  # Removes space at end of string





""" Tuples """

# Create tuple
coordinates = (4, 5)
print(coordinates)





""" While Loop """

# Create while loop
i = 1
while i <= 10:  # if this condition is met, then do actions below
    print(i)  # print i
    i += 1  # add 1 to i, which is the same as i = i+1
    # then start over and check if i+1 is still less than 10, and repeat

print('done')





""" Object Type """
type(df)
type(list)





" Scrape PDFs "
import glob
import pdfplumber
import pandas as pd
from tabulate import tabulate

" Single PDF "

# Import single PDF
single_pdf = pdfplumber.open("/Users/jeff/Documents/Python Projects/Earnings Statements/2021/els-01_02_2021 - Federal Energy Regulatory Commission.pdf")
single_page = single_pdf.pages[0]
single_pdf_text = single_page.extract_text()
print(single_pdf_text)

# Data type
type(single_pdf_text)

# Convert string to list
single_pdf_list = list(single_pdf_text.split())
print(single_pdf_list)

# Extract item from list
single_pdf_list[3]

# List to Dataframe
single_pdf_columns = ["Field"]
single_pdf_df = pd.DataFrame(single_pdf_list, columns=single_pdf_columns)
print(tabulate(single_pdf_df, headers='keys', tablefmt='plain'))

# Replace unnecessary characters with spaces
single_pdf_df['Field'] = single_pdf_df['Field']\
    .str.replace("\xa0", " ", regex=True)\
    .str.replace("\n", " ", regex=True)

# Source
# https://stackoverflow.com/questions/55767511/how-to-extract-text-from-pdf-in-python-3-7





""" Plot """

" Sankey Diagram "
# Dataframe needs source, sink, and volume columns
# For Sankey diagram, data needs to be broken up into 1) unique labels, 2) links between source, target, and value

import pandas as pd
import plotly.graph_objects as go

# Import dataframe with source, sink, and quantity columns
df = pd.read_csv("Sample Gas Flow Data - Sheet1.csv")

# Concatenate list of buyer and seller companies
buyers_sellers = pd.concat([df['Buyer'], df['Seller']], ignore_index=True)

# Unique companies as list
unique_companies = buyers_sellers.unique()

# Assign number to each unique company in list
label = {ni: indi for indi, ni in enumerate(set(unique_companies))}

# Convert dictionary to dataframe
label_key_df = pd.DataFrame(list(label.items()), columns=['Name', 'Key'])

# Merge back to original dataframe to populate buyer keys
df_key = df[['Buyer', 'Seller', 'Volume']].merge(
    label_key_df[['Name', 'Key']], how='left', left_on=['Buyer'], right_on=['Name'], suffixes=('_Buyer',
                                                                                               'Seller')).merge(
    label_key_df[['Name', 'Key']], how='left', left_on=['Seller'], right_on=['Name'], suffixes=('_Buyer', '_Seller'))

# Set colors
df_links = df[['Buyer', 'Seller']]  # Subset dataframe to source and target
df_colors = df_links.drop_duplicates(  # Dataframe of unique links between source and target
    subset=['Buyer', 'Seller'],
    keep='first').reset_index(drop=True)

# Set colors of individual companies
colors = ['#D8DEE9', '#E5E9F0', '#ECEFF4', '#D8DEE9', '#E5E9F0', '#ECEFF4', '#D8DEE9', '#E5E9F0', '#ECEFF4',
          '#D8DEE9', '#E5E9F0', '#ECEFF4',  '#D8DEE9', '#E5E9F0', '#ECEFF4', '#D8DEE9', '#E5E9F0', '#ECEFF4',
          '#D8DEE9', '#E5E9F0', '#ECEFF4', '#D8DEE9', '#E5E9F0', '#ECEFF4', '#D8DEE9', '#E5E9F0', '#ECEFF4', '#D8DEE9']

# Set color of links between source and target
color_link = ['#2E3440', '#3B4252', '#434C5E', '#4C566A', '#2E3440', '#3B4252', '#434C5E', '#4C566A', '#2E3440',
              '#3B4252', '#434C5E', '#4C566A', '#2E3440', '#3B4252', '#434C5E', '#4C566A', '#2E3440', '#3B4252',
              '#434C5E', '#4C566A', '#2E3440', '#3B4252', '#434C5E', '#4C566A', '#2E3440', '#3B4252', '#434C5E',
              '#4C566A']

# Add colors to dataframe with unique links
df_colors['Color'] = colors
df_colors['Color_Link'] = color_link

# Unique label key
key_label = list(label_key_df['Name'])
key_source = list(df_key['Key_Buyer'])
key_target = list(df_key['Key_Seller'])
key_volume = list(df_key['Volume'])

# Print
print(label_key_df)  # Dictionary key
print(key_label)  # Unique list of companies
print(key_source)
print(key_target)
print(key_volume)



# Plot
fig = go.Figure(data=[go.Sankey(
    valueformat=".0f",  # Don't show thousands "k"
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="white", width=8),
        label=key_label,
        color=df_colors['Color']
        ),
    link=dict(
        source=key_source,
        target=key_target,
        value=key_volume,
        color=df_colors['Color_Link'])
    )])

fig.update_layout(title_text="Gas Flows<br>Data from 760", font=dict(size=12, color='black'))
fig.show()



" Small Multiples 1 "
# http://jonathansoma.com/lede/data-studio/classes/small-multiples/long-explanation-of-using-plt-subplots-to-create-small-multiples/

import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=7, ncols=5, sharex=True, sharey=True, figsize=(10,10))
axes_list = [item for sublist in axes for item in sublist]

ordered_videos = df["Video"].head(32)
grouped = df.groupby("Video")

first_date = df['Date'].min()
last_date = df['Date'].max()

for video in ordered_videos:
    selection = grouped.get_group(video)

    ax = axes_list.pop(0)
    selection.plot(x='Date', y='Views', label=video, ax=ax, legend=False, clip_on=False)
    ax.set_title(video)
    ax.tick_params(
        which='both',
        bottom='off',
        left='off',
        right='off',
        top='off'
        )
    ax.grid(linewidth=0.25)
    ax.set_xlim((first_date, last_date))
    ax.set_xticks((first_date, last_date))
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    max_date = selection["Date"].max()
    views = float(selection[df_export["Date"] == max_date]["Views"])
    ax.set_ylim((0, 150000000))
    ax.scatter(x=[max_date], y=[views], s=70, clip_on=False, linewidth=0)
    ax.annotate(str(int(views/1000000)) + "M", xy=[max_date, views], xytext=[7, -2], textcoords='offset points')

for ax in axes_list:
    ax.remove()

plt.tight_layout()
plt.subplots_adjust(hspace=1)


" Small Multiples 2 "

# libraries

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# data
df = pd.DataFrame({
    'x_values': range(1, 101),
    'y_values': np.random.randn(100) * 15 + range(1, 101),
    'z_values': (np.random.randn(100) * 15 + range(1, 101)) * 2})

# initialise the figure. here we share X and Y axis
fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)
axes[0].plot('x_values', 'y_values', data=df, marker='o', alpha=0.4)
axes[1].plot('x_values', 'z_values', data=df, linestyle='none', marker='o', color="orange", alpha=0.3)
axes[0].title.set_text('These 2 plots have the same limit for the Y axis')

# Show the graph
plt.show()


" Small Multiples 3 "
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()


" Line graph "
my_x = np.linspace(-1, 1)
my_y = np.sin(my_x)
plt.plot(my_x, my_y)
title = 'Plot Name'
plt.title(title)




# Customize ticks
# https://e2eml.school/matplotlib_ticks.html#direction
