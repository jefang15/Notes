""" Python Notes - Graphs - Sankey Diagrams """



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
