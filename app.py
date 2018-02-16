from flask import Flask, render_template, request
import pandas as pd
from bokeh.charts import Histogram
from bokeh.embed import components
import time
from bokeh.layouts import gridplot, widgetbox,layout, row
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider, DataTable
from bokeh.plotting import figure

app = Flask(__name__)

# Load the Iris Data Set
iris_df = pd.read_csv("data/iris.data",
                      names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
feature_names = iris_df.columns[0:-1].values.tolist()

# create some widgets
slider = Slider(start=0, end=10, value=1, step=.1, title="Slider")
button_group = RadioButtonGroup(labels=["Option 1", "Option 2", "Option 3"], active=0)
select = Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])
button_1 = Button(label="Button 1")
button_2 = Button(label="Button 2")

w = widgetbox(button_1, slider, button_group, select, button_2, width=300)

# Create the main plot
#
x = list(range(11))
y0 = x


def create_figure():
    p = figure(plot_height=600, plot_width=700, title="", toolbar_location=None)

    p.circle(x, y0, size=10, color="navy", alpha=0.5)

    return p

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

    # Embed plot into HTML via Flask Render
#    script, div = components({'p':plot, 'wid':w})

    #p = figure(plot_height=600, plot_width=700)
    #l = layout([p])

    #data_table = DataTable(source=iris_df, width=800)

    script, div = components( row(w, plot))
    return render_template("vizualize.html", script=script, div=div,time_to_plot=time_to_plot)
                           #bins=bins, feature_names=feature_names, current_feature_name=current_feature_name)


# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
    app.run(port=5000, debug=True)

