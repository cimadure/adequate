from flask import Flask, render_template, request
from django.shortcuts import render, render_to_response


from bokeh.resources import INLINE

import pandas as pd
from bokeh.embed import components
import time
from bokeh.layouts import gridplot, widgetbox,layout, row
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider, DataTable,TableColumn, DateFormatter
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, CDSView, GroupFilter
from bokeh.models import Span, LabelSet
from functions import *

#from bokeh.io import output_file, show, vform

app = Flask(__name__)

# create some widgets
#rating = Slider(start=0, end=10, value=1, step=.1, title="Slider")
button_group = RadioButtonGroup(labels=["Average", "O/5", "5/5"], active=0)
#base_line = Select(title="minimal target :", value="Target", options=["IBM", "bar", "baz", "quux"])


w = widgetbox(button_group, width=300)

# Create the main plot
#
x = list(range(11))
y0 = x

hover = HoverTool(tooltips=[
    ("Name", "@index"),
])

#TOOLS = "box_select,lasso_select,hover,help"
TOOLS="crosshair,help,pan,box_zoom,reset,box_select,wheel_zoom,lasso_select"

target = 'Target'

def process_data():

    df = pd.read_csv("data/data_vendors.csv")
    df = reshape_data(df).transpose()

    train = df.loc[target]
    label_all = list(df.index)

    test = df[df.index != target]
    label_test = list(test.index)
    data = i_dont_know(test, train=train)
    #data = rescale_dimension(data)
    #df_sym = pd.DataFrame(data,columns=['x', 'y'], index=list("ABCDEF"))
    df_result = pd.DataFrame(data, columns=['x', 'y'], index=label_test)
    return df_result

df_result = process_data()


def create_figure():
    p = figure(plot_height=600, plot_width=700, title="", toolbar_location=None, tools=[hover, TOOLS])

    # df = pd.DataFrame(np.tile(np.array([1, 2, 3, 4, 5]), (3, 1)), columns=list('ABCDE'))
    # df = df.transpose()
    # df.loc['F'] = [3.5, 3.5, 3.5]
    # print(df)
    # train = df.loc['C']

    cds_data = ColumnDataSource(df_result)
    print(cds_data)

    target_view = CDSView(source=cds_data, filters=[GroupFilter(column_name='index', group=target)])

    p.circle(x="x", y="y", source=cds_data, size=10, color="navy", alpha=0.5, hover_color="red")
    p.circle(x="x", y="y", source=cds_data, size=10, color="red", alpha=0.5, hover_color="red")
    #p.add_layout(LabelSet(x='x', y='x', text='index', source=cds_data, x_offset=0.01, y_offset=0.01))

    for loc, dim in zip([0, 0], ['width', 'height']):
        p.add_layout(Span(location=loc, dimension=dim, #source=target_view,
                          line_color='green', line_dash='dashed', line_width=3))

    return p

df = pd.read_csv("data/data_vendors.csv")
#print(df)


columns = [
    #Category, Criteria, Target, Apple, IBM, HP, Huawei
    TableColumn(field='Category', title='cat Number'),
    TableColumn(field='Criteria', title='crit Number'),
    # TableColumn(field='Target', title='targ Number',),
    # TableColumn(field='Apple', title='ibm'),
    # TableColumn(field='IBM', title='hp'),
    # TableColumn(field='HP', title='hu'),
    # TableColumn(field='Huawei', title='app Mass')
]
column_names = [tc.field for tc in columns]
print(column_names)

#df = pd.DataFrame(np.random.randn(4, len(column_names)), columns=column_names)
print(df[column_names])
source = ColumnDataSource(df[column_names])
print(source)


# Index page
@app.route('/')
def index():
    # Create the plot, and time it
    t0 = time.time()
    plot = create_figure()
    t1 = time.time()
    time_to_plot = t1 - t0
    time_to_plot = "%.4f seconds" % time_to_plot

    data_table = DataTable(source=source, columns=columns)#, height=600, editable=True)
    table = widgetbox(data_table)

#    l = layout(children=[[plot],w,table])
    l = layout(children=[table])

    script, div = components(row(w, plot))
    #script, div = components(l)

    return render_template("vizualize.html", script=script, div=div,time_to_plot=time_to_plot)


def django_app(request):
    x= [1,3,5,7,9,11,13]
    y= [1,2,3,4,5,6,7]
    title = 'y = f(x)'

    plot = figure(title= title ,
        x_axis_label= 'X-Axis',
        y_axis_label= 'Y-Axis',
        plot_width =400,
        plot_height =400)

    plot.line(x, y, legend= 'f(x)', line_width = 2)
    #Store components
    script, div = components(plot)

    #Feed them to the Django template.
    return render_to_response( 'vizualize.html',
            {'script' : script , 'div' : div} )



from os.path import dirname, join

import pandas as pd

from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import RangeSlider, Button, DataTable, TableColumn, NumberFormatter
from bokeh.io import curdoc


resources = INLINE
js_resources = resources.render_js()
css_resources = resources.render_css()

#df = pd.read_csv(join(dirname(__file__), 'salary_data.csv'))

#df = pd.DataFrame(np.random.randn(4, 3), columns=['name',"salary","years_experience"])

df = pd.DataFrame([{'name': 'CA1', 'years_experience': "cr1", },
                   {'name': 'CA1', 'years_experience': "cr2", },
                   {'name': 'CA2', 'years_experience': "cr3", },
                   {'name': 'CA3', 'years_experience': "cr4", },
                   {'name': 'CA3', 'years_experience': "cr3", }])

source = ColumnDataSource(df)


from datetime import date
from random import randint

def tableau(request):

    #
    # #source = ColumnDataSource(data=dict())
    #
    # s1 = figure(width=250, plot_height=250, title=None)
    button = Button(label="Foo")
    #
    #
    # columns = [
    #     TableColumn(field="name", title="Employee Name"),
    #     #TableColumn(field="salary", title="Income", formatter=NumberFormatter(format="$0,0.00")),
    #     TableColumn(field="years_experience", title="Experience (years)")
    # ]
    #
    # data_table = DataTable(source=source, columns=columns, width=800)
    #
    # table = widgetbox(data_table)
    # l = layout([widgetbox(button)])
    # script, div = components(l)
    # print(script)
    # print(div)

    data = dict(
        dates=[date(2014, 3, i + 1) for i in range(10)],
        downloads=[randint(0, 100) for i in range(10)],
    )
    source = ColumnDataSource(data)

    columns = [
        TableColumn(field="dates", title="Date", formatter=DateFormatter()),
        TableColumn(field="downloads", title="Downloads"),
    ]
    data_table = DataTable(source=source, columns=columns, width=400, height=280)
    table = widgetbox(data_table)

    w1 = Slider(start=0, end=10, value=1, step=.1, title="Stuff")

    script, div = components(widgetbox(button_group, w1))

    return render_to_response('index.html',
                              {'title': 'Beautifulll',
                               'js_resources': js_resources, 'css_resources': css_resources,
                               'plot_script': script, 'plot_div': div})



    # Feed them to the Django template.
    #return render_to_response('vizualize.html',{'script': script, 'div': div})

# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
    #app.run(port=5000, debug=True)
    app.run(port=8000, debug=True)
    #app.run(debug=True)