
"""
TITLE: How to plot multiple bars next to each other
@author: Oluwatosin Odubanjo
"""

import matplotlib.pyplot as plt


dot = [0.0001627, 0.0001627, 0.0001627, 0.0001627, 0.0001627, 0.0001627, 0.0001627]

native_mm_list = 0.01565
opt_mm_list = 0.01331
native_mm_array = 0.07461
opt_mm_array = 0.05149


x = 1
width = 1

plt.plot(dot, color='#029386', linestyle='--',label='np.dot()')
plt.bar(x, native_mm_list, color = '#04D8B2',
        width = width, edgecolor = 'white', label = 'nat_mm_list')

plt.bar(x + width, opt_mm_list, color = '#15B01A',
        width = width, edgecolor = 'white', label ='opt_mm_list')

new_x = 4

plt.bar(new_x, native_mm_array, color = '#9A0EEA',
        width = width, edgecolor = 'white', label='nat_mm_array')

plt.bar(new_x + width, opt_mm_array, color = '#FF796C',
        width = width, edgecolor = 'white', label='opt_mm_array')


plt.ylabel("Time (in seconds)")
plt.xticks([1,2,4,5],['n_mm_l','o_mm_l','n_mm_a','o_mm_a'])
plt.title("SIZE = 30")
plt.legend(loc="upper left")
plt.show()
