""" Python Notes - List/Array """
# See Programming > LeetCode > Data Structures Notes for more notes on arrays.


" Create List "

# List of numbers
prime_numbers = [1, 3, 5, 7, 11, 13, 17, 19]
print(prime_numbers)

# List of strings
names_list = ['John', 'James', 'Joel']
print(names_list)

# Create list from dataframe column
key_volume = list(df['Volume'])



" Insert "

# Add item to list of strings
list.append('Cal')

# Add item to list of strings in a specific position
list.insert(0, 'Al')



" Other "

# Assign numbers to each item
# https://stackoverflow.com/questions/42350029/assign-a-number-to-each-unique-value-in-a-list
label = {ni: indi for indi, ni in enumerate(set(source_list))}
label_key = [label[ni] for ni in source_list]



" Indexing "

list = ['Apple', 'Banana', 'Orange']

print(list[0])  # First item in list
print(list[1])  # Second item in list
print(list[-1])  # Last from list
print(list[2:5])  # Range of items. Returns third, fourth, and fifth items
print(list[:4])  # First n items. Returns first through 4th item
print(list[4:])  # Last n items. Returns 4th through last item

" Delete "
# Remove item from list of strings
names_list.remove('Cal')
