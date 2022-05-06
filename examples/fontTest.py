import numpy as np
import pandas as pd
import chartify

data = chartify.examples.example_data()

quantity_by_fruit_and_country = (data.groupby(
    ['fruit', 'country'])['quantity'].sum().reset_index())

country_order = (
    quantity_by_fruit_and_country.groupby('country')['quantity'].sum()
        .sort_values(ascending=False).index)

quantity_by_fruit_and_country['label'] = np.where(
    quantity_by_fruit_and_country['fruit'].isin(['Banana', 'Orange', 'Grape', 'Apple']),
    quantity_by_fruit_and_country['quantity'],
    None)

# apple total=608
apples = quantity_by_fruit_and_country[quantity_by_fruit_and_country['fruit'] == "Apple"]
appleQuantity = apples['quantity']
appleTotal = appleQuantity.sum()

banana = quantity_by_fruit_and_country[quantity_by_fruit_and_country['fruit'] == "Banana"]
bananaQuantity = banana['quantity']
bananaTotal = bananaQuantity.sum()

grape = quantity_by_fruit_and_country[quantity_by_fruit_and_country['fruit'] == "Grape"]
grapeQuantity = grape['quantity']
grapeTotal = grapeQuantity.sum()

orange = quantity_by_fruit_and_country[quantity_by_fruit_and_country['fruit'] == "Orange"]
orangeQuantity = orange['quantity']
orangeTotal = orangeQuantity.sum()

# print(quantity_by_fruit_and_country)
quantity_by_fruit_and_country.insert(4, "fruit total", [appleTotal, None, None, None, None,
                                                        bananaTotal, None, None, None, None,
                                                        grapeTotal, None, None, None, None,
                                                        orangeTotal, None, None, None, None], False)

ch = chartify.Chart(blank_labels=True, x_axis_type='categorical')
ch.set_title("Grouped bar chart - Ordered stack")
ch.set_subtitle("Banana Total: " + str(bananaTotal) +
                " Orange Total: " + str(orangeTotal) +
                " Apple Total: " + str(appleTotal) +
                " Grape Total: " + str(grapeTotal))
ch.plot.bar_stacked(
    data_frame=quantity_by_fruit_and_country,
    categorical_columns=['fruit'],
    numeric_column='quantity',
    stack_column='country',
    normalize=False,
    stack_order=country_order,
    font='times')

ch.plot.text_stacked(
    data_frame=quantity_by_fruit_and_country,
    categorical_columns=['fruit'],
    numeric_column='quantity',
    stack_column='country',
    text_column='label',
    normalize=False,
    stack_order=country_order,
    # Set the text color otherwise it will take
    # The next color in the color palette.
    text_color='white'
)

ch.show()
