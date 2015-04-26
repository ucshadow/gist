__author__ = 'SHADOW'

import matplotlib.pyplot as plt
import os
import pandas as pd
from collections import Counter
from pylab import rcParams
import matplotlib.ticker as plticker

plt.style.use('ggplot')

rcParams['figure.figsize'] = 18, 14
plt.rcParams['figure.edgecolor'] = 'r'
plt.rcParams['grid.alpha'] = '0'
plt.rcParams.update({'font.size': 14})
loc = plticker.MultipleLocator(base=1.0)

os_ = os.getcwd() + '\graphs\\'

ops = open("OP's.txt", 'r').read().split()

op_number = Counter(ops)
posts = []
names = sorted(op_number, key=op_number.get, reverse=True)[:10]
for i in names:
    posts.append(int(op_number[i]))


s = pd.Series(posts, index=names)

plt.title('Top posters')
plt.ylabel('Number of posts', fontsize=15)
plt.xlabel('')

ax = plt.gca()
ax.tick_params(axis='x', colors='blue')
ax.tick_params(axis='y', colors='#093B61')
ax.set_ylim([0, posts[0] + 1])
ax.tick_params(axis='y', labelsize=16)
ax.yaxis.set_major_locator(loc)
ax.yaxis.grid(True, alpha=0.3, color='pink')

ax2 = plt.gca()


color_codes = ['#651505', '#651505', '#651505', '#651505',
               '#651505', '#651505', '#501c06', '#402207',
               '#3a2407', '#312809', '#292a09',
               '#242c0a', '#1d2f0a', '#18310b', '#12320b'
               '#242c0a', '#1d2f0a', '#18310b', '#12320b'
               '#651505', '#651505', '#651505', '#651505',
               '#651505', '#651505', '#501c06', '#402207',
               '#3a2407', '#312809', '#292a09',
               '#242c0a', '#1d2f0a', '#18310b', '#12320b'
               '#242c0a', '#1d2f0a', '#18310b', '#12320b']

set_colors = []
for score in posts:
    set_colors.append(color_codes[score])

graph = pd.Series.plot(s, kind='bar', color=set_colors, width=0.85, alpha=1)
graph.set_xticklabels(s.index, rotation=0, fontsize=14)
graph.set_axis_bgcolor('black')

filename = 'total karma per mean karma'
path = (os_ + filename)
fig = graph.get_figure()

plt.tight_layout()
plt.savefig(path)
