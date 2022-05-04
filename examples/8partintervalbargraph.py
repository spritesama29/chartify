import pandas as pd
import chartify

example_data = pd.DataFrame(
    list(zip(
        ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
        ['A', 'A', 'B', 'B', 'A', 'A', 'B', 'B'],
        ['c', 'd', 'c', 'd', 'c', 'd', 'c', 'd'],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [v + 0.1 for v in [1, 2, 3, 4, 5, 6, 7, 8]],
        [v - 0.1 for v in [1, 2, 3, 4, 5, 6, 7, 8]]
    )),
    columns=['cat_1', 'cat_2', 'cat_3', 'val', 'upper', 'lower']
)

ch = chartify.Chart(blank_labels=True, x_axis_type='categorical')
ch.plot.bar(
    data_frame=example_data,
    categorical_columns=['cat_1', 'cat_2', 'cat_3'],
    numeric_column='val'
)
ch.plot.interval(
    data_frame=example_data,
    categorical_columns=['cat_1', 'cat_2', 'cat_3'],
    lower_bound_column='lower',
    upper_bound_column='upper',
)
ch.show()
