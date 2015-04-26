import matplotlib.pylab as plt
import json
import numpy as np
from pylab import rcParams
import matplotlib.ticker as plticker
import pandas

with open('op_karma.json') as f:
    ops = json.loads(f.read())


top_karma = sorted(ops.keys(), key=lambda ee: ops[ee][0], reverse=True)[:10]

op_names = []
total_karma = []
medium_karma = []
total_posts = []

for i in top_karma:
    op_names.append(i)
    total_karma.append(ops[i][0])
    medium_karma.append(int(ops[i][0] / ops[i][1]))
    total_posts.append(ops[i][1])

print(op_names)
print(total_karma)
print(medium_karma)
print(total_posts)

plt.style.use('ggplot')

rcParams['figure.figsize'] = 18, 14
plt.rcParams['figure.edgecolor'] = 'r'
plt.rcParams['grid.alpha'] = '0'
loc = plticker.MultipleLocator(base=100.0)


color_codes = ['#651505', '#651505', '#501c06', '#402207',
               '#3a2407', '#312809', '#292a09',
               '#242c0a', '#1d2f0a', '#18310b', '#12320b']

set_colors = []

for score in range(len(top_karma)):
    set_colors.append(color_codes[len(total_karma) - score])

width = 0.4
df = pandas.DataFrame(dict(graph=op_names,
                           n=total_karma,
                           m=medium_karma))

ind = np.arange(len(df))

fig, ax = plt.subplots()
ax.bar(ind, df.n, width, color=set_colors)
ax.bar(ind + width, df.m, width, color='g')
ax.set(xticks=ind + width, xticklabels=df.graph, xlim=[2 * width - 1, len(df)],
       title='total karma and median karma by poster')
ax.set_axis_bgcolor('black')
ax.tick_params(axis='x', colors='blue')
ax.tick_params(axis='y', colors='#093B61')
ax.set_ylim([0, total_karma[0] + 50])
ax.tick_params(axis='y', labelsize=16)
ax.yaxis.set_major_locator(loc)
ax.yaxis.grid(True, alpha=0.3, color='pink')


plt.show()

