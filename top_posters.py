__author__ = 'SHADOW'

from collections import Counter
import pygal


ops = open("OP's.txt", 'r').read().split()


op_number = Counter(ops)
posts = []
names = sorted(op_number, key=op_number.get, reverse=True)[:10]
for i in names:
    posts.append(int(op_number[i]))


for top in range(len(posts)):
    print('user ', names[top], 'has ', posts[top], ' posts')

from pygal.style import Style
custom_style = Style(
  background='transparent',
  plot_background='#333333',
  foreground='#3b5998',
  foreground_light='#162d5c',
  foreground_dark='#198336',
  opacity='1',
  opacity_hover='.9',
  transition='400ms ease-in',
)

chart = pygal.Bar(fill=True, interpolate='cubic', style=custom_style, width=1280, height=800,
                  include_x_axis=True, y_title='number of posts',
                  title_font_size=30, show_dots=False, label_font_size=14)
chart.title = 'top posters'
for x in range(10):
    chart.add(names[x], posts[x])
chart.render_to_file('top_posters.svg')