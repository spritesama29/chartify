import chartify

data = chartify.examples.example_data()

quantity_by_fruit = (data.groupby('fruit')['quantity'].sum().reset_index())
print(quantity_by_fruit.head())
quantity_by_fruit.at[0,"fruit"] = "magmaMace"
quantity_by_fruit.at[1,"fruit"] = "LeorioKnig"
quantity_by_fruit.at[2,"fruit"] = "Kurapika00"
quantity_by_fruit.at[3,"fruit"] = "OysterCrkr"
ch = chartify.Chart(False, y_axis_type='categorical')
ch.set_title("Vertical bar plot")
ch.set_source_label("I am a source label!")
ch.plot.bar(
data_frame=quantity_by_fruit,
categorical_columns='fruit',
numeric_column='quantity')
#print(quantity_by_fruit.get('fruit')[0])
ch.show()
