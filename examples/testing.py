import chartify


#Hey all, if you're reading this, please make your own testing file so we can have many files to look back on.
data = chartify.examples.example_data()
#print(data.head())

ch = chartify.Chart(blank_labels=True, y_axis_type='density')
ch.set_title("Histogram")
ch.set_subtitle("")
ch.plot.histCumu(data_frame=data,values_column='unit_price',bins='auto',method='count')
ch.show()

