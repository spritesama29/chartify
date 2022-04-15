import chartify

data = chartify.examples.example_data()

quantity_by_fruit = (data.groupby('fruit')['quantity'].sum().reset_index())
print(quantity_by_fruit.head())
quantity_by_fruit.iloc[0,0] = 'AAAAAAAAAAAAAAAAAAAA'
ch = chartify.Chart(False, y_axis_type='categorical')
ch.set_title("Vertical bar plot")
ch.plot.bar(
data_frame=quantity_by_fruit,
categorical_columns='fruit',
numeric_column='quantity')
print(quantity_by_fruit.get('fruit')[0])
ch.show()
