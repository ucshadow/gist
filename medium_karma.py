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
loc = plticker.MultipleLocator(base=10.0)

os_ = os.getcwd() + '\graphs\\'

with open('dict_storage.json') as f:
    idol_list = json.loads(f.read())

prelim_g2 = {}
prelim = {}

for pre_i in idol_list:
    if idol_list[pre_i][2] >= 2:
        prelim_g2[pre_i] = idol_list[pre_i][1]

for candidate in prelim_g2:
    try:
        prelim[candidate] = int(idol_list[candidate][1] / idol_list[candidate][2])
    except ZeroDivisionError:
        prelim[candidate] = 0

medium_karma = sorted(prelim.items(), key=lambda x: x[1], reverse=True)[:10]

m_name = []
m_karma = []
m_posts = []
name_posts = []

for yah in medium_karma:
    m_name.append(yah[0])
    m_karma.append(yah[1])

for upvote in m_name:
    m_posts.append(idol_list[upvote][2])

for num in range(len(m_name)):
    name_posts.append(m_name[num] + '-' + str(m_posts[num]))

panda = pd.Series(m_karma, index=name_posts)

plt.title('medium karma per post for idols with 2 or more posts')
plt.ylabel('karma', fontsize=14)
plt.xlabel('idol and number of times posted', fontsize=14)

ax = plt.gca()
ax.tick_params(axis='x', colors='blue')
ax.tick_params(axis='y', colors='#093B61')
ax.set_ylim([0, m_karma[0] + 50])
ax.tick_params(axis='y', labelsize=16)
ax.yaxis.set_major_locator(loc)
ax.yaxis.grid(True, alpha=0.3, color='pink')
ax.legend_ = None

color_codes = ['#651505', '#651505', '#501c06', '#402207',
               '#3a2407', '#312809', '#292a09',
               '#242c0a', '#1d2f0a', '#18310b', '#12320b']

set_colors = []
for score in range(len(m_karma)):
    set_colors.append(color_codes[len(m_karma) - score])


graph = pd.Series.plot(panda, kind='bar', color=set_colors, width=0.8, alpha=1)
graph.set_xticklabels(panda.index, rotation=0, fontsize=14)
graph.set_axis_bgcolor('black')

filename = 'medium Karma per post'
path = (os_ + filename)
fig = graph.get_figure()

plt.tight_layout()
plt.savefig(path)

