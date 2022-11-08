import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
# Create a slider using for
x = np.arange ( 5 )
y0 = x + 0
y1 = x + 1
y2 = x + 2
# store plot contents in array elements
plot = [
    go.Scatter ( x=x, y=y0, name= ' y0' ) ,
    go.Scatter ( x=x, y=y1, name= ' y1' ) ,
    go.Scatter ( x=x, y=y2, name= ' y2' ) ,
]
# create slider content
steps = []
for num, _ in enumerate ( plot ) :
    # Hide all plots once, then show the corresponding plots
    visible = [ False ] * len ( plot )
    visible [ num ] = True
    step = dict (
        label=num,   # slider label
        method= 'update' ,   # slider applies to data plots and layouts
        args= [
            dict ( visible=visible ) ,   # show only y0
        ]
    )
    steps. append ( step )
# create a slider to put in the layout
sliders = [
    dict (
        active= 0 ,   # index of plot to display in initial state
        # display the slope of each slider above the slider
        currentvalue= dict ( prefix= 'intercept = ' ) ,
        steps=steps,
        len= 0.5 ,   # Length of slider
    )
]
# create layout
layout = go.Layout (
    font_size= 20 ,   # Font size for the entire graph
    hoverlabel_font_size= 20 ,   # hover font size
    yaxis_range= ( 0 , 8 ) ,   # vertical axis display range
    sliders=sliders   # place sliders
)
# display the graph
fig = go.Figure ( data =plot, layout=layout )
fig. show ()