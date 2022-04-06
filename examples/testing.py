import chartify
import numpy as np
import pandas as pd


import matplotlib.pyplot as plt
#Hey all, if you're reading this, please make your own testing file so we can have many files to look back on.


#data = chartify.examples.example_data()
#print(data.head())
#ch = chartify.Chart(blank_labels=True, y_axis_type='density')
#ch.set_title("Histogram")
#ch.set_subtitle("")
#ch.plot.box(data_frame=data)
#ch.plot.histCumu(data_frame=data,values_column='unit_price',bins='auto',method='count')
#ch.show()

ch = chartify.Chart(blank_labels=True, y_axis_type='density')
np.random.seed(10)
data = np.random.normal(100, 20, 200)
ch.set_title("Da Box")
ch.set_subtitle("")
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['Col1', 'Col2', 'Col3', 'Col4'])


ch.show()
