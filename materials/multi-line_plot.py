#%%
import pandas as pd
from sklearn.datasets import load_iris
import holoviews as hv
from bokeh.io import output_file, show, save
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.models import HoverTool
from bokeh.palettes import Category10
import hvplot.pandas 
import numpy as np 
from itertools import chain

#Set up the data
group = np.repeat(['Group 1', 'Group 2','Group 3'], 10)
x = list(range(1,11))*3
y = np.random.randint(10, size=30)

df = pd.DataFrame(
    {'group': group,
     'x': x,
     'y': y
    })

#hvplot
p1= df.hvplot('x','y',by='group')
hvplot.show(p1)


#bokeh - loop through column data source
p2 = figure(plot_width=600, plot_height=300)

grp_list = df.group.unique()
for i in range(len(grp_list)):

    source = ColumnDataSource(
        data={
            'x':df.loc[df.group == grp_list[i]].x,
            'group':df.loc[df.group == grp_list[i]].group,
            'y':df.loc[df.group == grp_list[i]].y})
    
    p2.line(
             x='x', 
             y='y',
             source=source,
             legend = grp_list[i],
             color = (Category10[3])[i])
              
hover = HoverTool(tooltips =[
    ('group','@group'),
    ('x','@x'),
    ('y','@y')])
p2.add_tools(hover)
show(p2)

#bokeh - multi_line

grp_list = df.group.unique()
xs = [df.loc[df.group == i].x for i in grp_list]
ys = [df.loc[df.group == i].y for i in grp_list]

source = ColumnDataSource(data=dict(
        x = xs, 
        y = ys,
        color = (Category10[3])[0:len(grp_list)],
        group = grp_list))


p3 = figure(plot_width=600, plot_height=300)

p3.multi_line(
        xs='x', 
        ys='y',
        legend='group',
        source=source,
        line_color='color')

#Add hover tools, basically an invisible line
source2 = ColumnDataSource(dict(
        invisible_xs=df.x,
        invisible_ys=df.y,
        group = df.group)) 

line = p3.line(
        'invisible_xs', 
        'invisible_ys',
        source=source2,
        alpha=0)

hover = HoverTool(tooltips =[
    ('group','@group'),
    ('x','@x'),
    ('y','@y')])
hover.renderers = [line]

p3.add_tools(hover)
show(p3)

#bokeh - loop through CDSView
p4 = figure(plot_width=600, plot_height=300)
source = ColumnDataSource(df)
grp_list = df.group.unique()
for i in range(len(grp_list)):

    view=CDSView(source=source, filters=[GroupFilter(column_name='group', group=grp_list[i])]) 
    p4.line(
        x='x', 
        y='y',
        source=source,
        view=view,
        legend = grp_list[i],
        color = (Category10[3])[i])

hover = HoverTool(tooltips =[
        ('group','@group'),
        ('x','@x'),
        ('y','@y')])
p4.add_tools(hover)
show(p4)