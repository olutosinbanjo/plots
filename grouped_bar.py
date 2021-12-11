
"""
TITLE: grouped bar plots
@author: Oluwatosin S. Oluseyi , December, 11, 2021
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

USM = [1.4181, 2.1281, 6.4723]
USM2 = [0.008686, 0.6534, 4.96424]
BUFFER = [1.5021, 2.3673, 7.8112]

n = len(USM)
x = np.arange(n)
width = 0.2

plt.bar(x, USM, color = '#04D8B2',
        width = width, edgecolor = 'white', label='getrs_usm_het1')

plt.bar(x + width, USM2, color = '#15B01A',
        width = width, edgecolor = 'white', label ='getrs_usm_het2')

plt.bar(x + width*2, BUFFER, color = '#9A0EEA',
        width = width, edgecolor = 'white', label ='getrs_buffer_het1')


plt.yscale('log')
plt.ylabel("Time (in seconds)")
plt.xticks(x+width,['500','2500','5000'])
plt.title("{USM Heterogeneous Version 1} VERSUS {USM Heterogeneous Version 2} VERSUS {BUFFER Heterogeneous Version 1}")
plt.legend(loc="upper left")

# BAR ANNOTATION (see https://www.pythoncharts.com/matplotlib/grouped-bar-charts-matplotlib/)
for bar in ax.patches:
  # The text annotation for each bar should be its height.
  bar_value = bar.get_height()
  # Format text for bars
  text = f'{bar_value}'
  # This will give the middle of each bar on the x-axis.
  text_x = bar.get_x() + bar.get_width() / 2
  # get_y() is where the bar starts so we add the height to it.
  text_y = bar.get_y() + bar_value
  # make text the same color as the bar
  bar_color = bar.get_facecolor()
  # If you want a consistent color, you can just set it as a constant, e.g. #222222
  ax.text(text_x, text_y, text, ha='center', va='bottom', color=bar_color,
          size=5)
  
plt.show()
