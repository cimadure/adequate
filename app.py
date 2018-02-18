from flask import Flask, render_template, request
import pandas as pd
from bokeh.embed import components
import time
from bokeh.layouts import gridplot, widgetbox,layout, row
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider, DataTable,TableColumn
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, CDSView, GroupFilter
from bokeh.models import Span, LabelSet
from functions import *

app = Flask(__name__)

# Load the Iris Data Set
iris_df = pd.read_csv("data/iris.data",
                      names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
feature_names = iris_df.columns[0:-1].values.tolist()

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
    # # Determine the selected feature
    # current_feature_name = request.args.get("feature_name")
    # if current_feature_name == None:
    #     current_feature_name = "Sepal Length"
    #
    # # Determine the number of bins
    # bins = request.args.get("bins")
    # if bins == "" or bins == None:
    #     bins = 10
    # else:
    #     bins = int(bins)

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
                           #bins=bins, feature_names=feature_names, current_feature_name=current_feature_name)


# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
    #app.run(port=5000, debug=True)
    app.run(port=8000, debug=True)
    #app.run(debug=True)