""" Python Notes - General """



" Check Python Version "
import sys
print(sys.version)
# 3.9.3 (v3.9.3:e723086bc3, Apr  2 2021, 08:25:55)
print(sys.executable)



" Call Packages "
# Download packages: run 'pip install package_name' in Terminal
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession  



" Import and Export Data (Save Data) "

# Import CSV
df = pd.read_csv("YouTube Views.csv")
# Import Excel
df = pd.read_excel("YouTube Views.xlsx")

# Export CSV
df.to_csv("YouTube Views.csv", index=False)

# Export Excel
df.to_excel("YouTube Views.xlsx", index=False)



" Operators "

# Not equal: !=



" Length "

# Number of rows in dataset
len(df)

# Length of string
len('Hello, world')

# Length of list
names_list = ['John', 'James', 'Joel']
len(names_list)
