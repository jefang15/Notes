
#!/usr/bin/env/python3


""" Visual Studio Code """

# Open Command Palette: Shift + Command + P
# Change Color Scheme: Open Command Palette > type color > select Color Theme
# Comment: # or """ """``
# Edit Keybindings: Search (Command + P) for JSON > select keybindings.json > enter/edit keybindings
# Edit Macros: Search (Command + P) from JSON > select settings.json > enter/edit macros
# If "import" command not found: type python3 and run 
# Jupyter Code Cell: #%%
# Jupyter Notebook: Command + Shift + P > Jupyter
# Open Command Palette: Command + Shift + "Jupyter: Create New Blank Workbook"
# Open Interactive Window: Control + I
# Run code in Interactive Window: shift + Enter
# Run code in Terminal: control + enter
# Search: Command + P
# Settings: Command + ,
# Terminal: ^'
# View Variables in Variable Explorer/Data Viewer: add cell to debug (run code to import packages in Interactive window if)
# Install extensions: click Extensions icon on Side Bar, or Shift + Command + X
# Install package/module: Open terminal, run "pip install ___"


""" GitHub """

" Run Git in Git Bash Terminal "
# Open Terminal: top bar
# Set directory: cd 'file path to folder in question on local computer'



"""
Create Repo

1. Create repo at: https://github.com/new

2. Create .gitignore file and populate
.DS_Store

3. Open Git Bash Terminal and set directory to folder you want the new repo in: 

cd '/Users/jeff/Documents/Programming/Projects'

4. Copy new repo link from GitHub Enterprise

5. In Git Bash Terminal, clone repo:

git clone 'https://github.com/jefang15/Scrape-Youtube-Views.git'

6. Set directory to new repo

cd scrape-youtube-views

7. Create and switch to new branch

git branch branch_name
then 
git checkout branch_name
or just use
git checkout -b branch_name

8. Do work in branch, or add files and folders to branch

9 Show status

git status

10. Add new files and changes to Staging Area

git add .

11. Commit (move content from Staging Area to Local Repository)

git commit -m 'commit_description'

12. Push changes to current branch

git push --set-upstream origin branch_name

12. Merge pull request

git checkout main
git merge working_branch
git push origin main





"""



# Set .gitignore as global in parent folder: git config --global core.excludesfile ~/.gitignore
# Remove a file that was added to .gitignore but is already on GitHub: 
#   Open Git Bash for folder/project that the file is in (see previous instructions) > Terminal
#   Delete: git rm --cached 'folder/file_name.file_type' (may not need folder name/ if file is not in folder)
#       e.g. git rm --cached 'Youtube Views/Small Multiples Views Chart 20210425.png' (copy reltive file path)
#       Successful if terminal reads: rm 'folder/file_name.file_type'
#   Commit change: git commit -m 'Name of commit here'
#   Push: git push origin branch_name
# Remove a folder:
#   Delete: git rm -r folder_name
# Remove a sub folder/directory: 
#   Delete: git rm -r 'Expenses/Earnings Statements'
#   Commit
#   Push: git push

# Remove contents from subfolder out and into new repo
# Set git bash terminal to location of new repo
# Check current repo location: ls
# Change git bash directory location: cd '/Users/jeff/Documents/Python/Python Projects'
# git clone 'file path of repo to duplicate' cloned_repo_name
# git remote rm origin  # detach cloned repo from original repo
# git remote -v  # show repo origin location
# Create new repo on GitHub Enterprise
# Create branch: git branch branch_name
# Set origin of cloned repo to the newly created repo: git remote add origin https://github.com/jefang15/Youtube-Views.git
# Push changes: git push -u origin main_branch
# New repo on Github Enterprise should now be populated
# Set directory to parent Python Projects folder: cd '/Users/jeff/Documents/Python/Python Projects'
# Copy new repo url from GitHub Enterprise and clone to local computer: git clone 'https://github.com/jefang15/Youtube-Views.git'
# Create branch: git branch branch_name
# Set directory to new repo location on desktop and clear out unwanted files and move up files to keep
# Delete: git rm -r 'file_or_folder_name'
# Move file up within a repo: go to GitHub Enterprise. Go to file, click edit, then type ../ before file name to move up.


""" Check Python Version """
import sys
print(sys.version)
# 3.9.3 (v3.9.3:e723086bc3, Apr  2 2021, 08:25:55)
print(sys.executable)

""" Packages """
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np





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





""" Class """
# Creates a new data type (beside string, numeric, boolean)

class student: # Student - name of class
    def __init__(self, name, major, gpa): # initialize function and define "student"
        self.name = name # each student has a name
        self.major = major # each student has a major
        self.gpa = gpa # each student has a gpa

# Objects within the class
student1 = student('Jim', 'Business', 4.0) # student1 is an object - an actual student
print(student1.name) # can call specific qualities of this student





""" DataFrame """

df=pd.DataFrame({
    'x_values': range(1,101), 
    'y_values': np.random.randn(100)*15+range(1,101), 
    'z_values': (np.random.randn(100)*15+range(1,101))*2 })





""" Dictionary """
# Dictionary keys (keys can be numbers or strings) must be unique

# Create dictionary
month_conversions = {
    'Jan':'January',
    'Feb':'February',
    'Mar':'March'
    # 'Jan' - key
    # 'January' - value
}

# Print specific value based on the key
print(month_conversions['Jan'])





""" Functions """

# Sample function
def bio(name, age):
    print(name + " is " + age + " years old.")
    # def - call function
    # greet - name of function
    # name - what to include when calling this function

bio('John', '35')





""" Lists """

# Create list of numbers
prime_numbers = [1,3,5,7,11,13,17,19]
print(prime_numbers)

# Create list of strings
names_list = ['John', 'James', 'Joel']
print(names_list)

# Add item to list of strings
names_list.append('Cal')

# Add item to list of strings in a specific position
names_list.insert(0, 'Al')

# Remove item from list of strings
names_list.remove('Cal')





""" Length """

# Length of string
len('Hello, world')

# Length of list
names_list = ['John', 'James', 'Joel']
len(names_list)





""" Loops """

" For Loop "
friend = ['Jim', 'Kristne', 'Tim']
for name in friend: # for every name in the friend list, do
    print(name) # print





" While Loop "

# Create while loop
i = 1
while i <= 10: # if this condition is met, then do actions below
    print(i) # print i
    i += 1 # add 1 to i, which is the same as i = i+1
    # then start over and check if i+1 is still less than 10, and repeat

print('done')





""" Tuples """

# Create tuple
coordinates = (4,5)
print(coordinates)





""" Plot """


# Small Multiples Graph 

# libraries

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# data
import pandas as pd
df=pd.DataFrame({
    'x_values': range(1,101), 
    'y_values': np.random.randn(100)*15+range(1,101), 
    'z_values': (np.random.randn(100)*15+range(1,101))*2 })

# initialise the figure. here we share X and Y axis
fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)
axes[0].plot('x_values', 'y_values', data=df, marker='o', alpha=0.4)
axes[1].plot('x_values', 'z_values', data=df, linestyle='none', marker='o', color="orange", alpha=0.3)
axes[0].title.set_text('These 2 plots have the same limit for the Y axis')


# Show the graph
plt.show()





