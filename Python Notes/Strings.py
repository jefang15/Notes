""" Python Notes - Strings """



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



" Regex "

# Split string by word instead of characters
pdf_text_words = pdf_text.split()

# Remove characters from string / keep only numeric
df['Column'] = df['Column'].extract('(\d+)')

# Replace symbols in string
new_data['Title'] = new_data['Title'].str.replace(".*(- )", "")  # Remove everything before hyphen via .* before the parentheses.
new_data['Title'] = new_data['Title'].str.replace("(\().*", "")  # Remove everything after the first open parenthesis
# "/("
new_data['Title'] = new_data['Title'].str.replace("(ft.).*","")   # Remove everything after the string "ft."
new_data['Title'] = new_data['Title'].str.rstrip(" ")  # Removes space at end of string
