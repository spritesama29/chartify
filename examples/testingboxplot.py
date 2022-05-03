import bokeh.io
import chartify

ch = chartify.Chart(blank_labels=True, y_axis_type='density')
list_equals = ["this is boxplot"]
data = [1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 13, 23]
p = ch.plot.box_plot(list_equals, data)
ch.show("preMade", p)
