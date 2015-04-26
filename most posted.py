__author__ = 'SHADOW'

import matplotlib.pyplot as plt
import os
import pandas as pd
import json
from pylab import rcParams
import matplotlib.ticker as plticker

plt.style.use('ggplot')

rcParams['figure.figsize'] = 18, 14
plt.rcParams['figure.edgecolor'] = 'r'
plt.rcParams['grid.alpha'] = '0'
loc = plticker.MultipleLocator(base=1.0)



os_ = os.getcwd() + '\graphs\\'

with open('dict_storage.json') as f:
    idol_list = json.loads(f.read())
scores = []
names_k = []

names = sorted(idol_list.keys(), key=lambda e: idol_list[e][0], reverse=True)[:10]
for i in names:
    scores.append(idol_list[i][0])
    names_k.append(i + '-' + str(int(idol_list[i][1] / idol_list[i][2])))

color_codes = ['#651505', '#651505', '#501c06', '#402207',
               '#3a2407', '#312809', '#292a09',
               '#242c0a', '#1d2f0a', '#18310b', '#12320b']

set_colors = []
for score in scores:
    set_colors.append(color_codes[score])

s = pd.Series(scores, index=names_k)

plt.title('Most posted')
plt.ylabel('Number of posts', fontsize=18)
plt.xlabel('Idol / mean karma (mean karma = total karma / number of posts)', fontsize=16)

ax = plt.gca()
ax.tick_params(axis='x', colors='blue')
ax.tick_params(axis='y', colors='#093B61')
ax.set_ylim([0, scores[0] + 1])
ax.tick_params(axis='y', labelsize=16)
ax.yaxis.set_major_locator(loc)
ax.yaxis.grid(True, alpha=0.3, color='pink')




graph = pd.Series.plot(s, kind='bar', color=set_colors, width=0.8, alpha=1)
graph.set_xticklabels(s.index, rotation=0, fontsize=16)
graph.set_axis_bgcolor('black')

filename = 'most posted.png'
path = (os_ + filename)
fig = graph.get_figure()

plt.tight_layout()
plt.savefig(path)





