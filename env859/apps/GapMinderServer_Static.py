'''
Instead of showing our plot to the screen (via "output_notebook()"),
we construct document ("curdoc") and add our plot ("p") to that. 
'''

##-----------IMPORTS--------------------
#Import the curdoc object 
from bokeh.io import curdoc 

#Import the figure object
from bokeh.plotting import figure

#Import models
from bokeh.models import (
    ColumnDataSource, 
    HoverTool, 
    LinearInterpolator, 
    CategoricalColorMapper
)

#Import all color palettes
from bokeh.palettes import *

##----------DATA-------------------------    
#import the data as a dataframe then as a ColumnDataSource object
import pandas as pd
data = pd.read_csv('../data/gapminder.csv',thousands=',',index_col='Year')
theCDS = ColumnDataSource(data.loc[2010])
    
##----------PLOT-------------------------  
#Create a styling dictionary for our plot
PLOT_OPS = {'title':'2010',
            'height':500,
            'width':1000,
            'x_axis_type':'log'}

#Create the population size mapper
size_mapper = LinearInterpolator(x=[data.loc[2010]['population'].min(),
                                    data.loc[2010]['population'].max()],
                                 y=[5,50])
    
#Create the region color mapper
color_mapper = CategoricalColorMapper(factors=data.loc[2010]['region'].unique(),
                                      palette=Spectral6)

hover = HoverTool(tooltips='@Country')
p = figure(**PLOT_OPS)
p.circle(x='income',
         y='life',
         source=theCDS,
         size={'field':'population','transform':size_mapper},
         color={'field':'region','transform':color_mapper},
         alpha=0.6,
         legend='region'
        )
p.legend.border_line_color = 'red'
p.right = p.legend


curdoc().add_root(p)