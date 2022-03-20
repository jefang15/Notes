""" Python Notes - Graphs - Small Multiples """



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
